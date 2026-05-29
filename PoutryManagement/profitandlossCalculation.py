import json
import pickle
import csv
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
import numpy as np
from decimal import Decimal, ROUND_HALF_UP
import os
from collections import defaultdict
import time
from functools import lru_cache

# ========== ENUMS & DATA CLASSES (OOP Concepts) ==========

class FeedType(Enum):
    """Enum for different types of feed"""
    STARTER = "starter"
    GROWER = "grower"
    FINISHER = "finisher"

class ExpenseCategory(Enum):
    """Enum for expense categories"""
    FEED = "Feed"
    MEDICAL = "Medical"
    LABOR = "Labor"
    UTILITIES = "Utilities"
    CAPITAL = "Capital"
    OTHER = "Other"

@dataclass
class Feed:
    """Feed class representing different feed types"""
    feed_type: FeedType
    initial_quantity: float
    used_quantity: float = 0.0
    price_per_kg: float = 0.0
    total_cost: float = field(init=False)
    remaining_quantity: float = field(init=False)
    
    def __post_init__(self):
        self.validate_quantities()
        self.calculate_quantities()
    
    def validate_quantities(self):
        """Validate feed quantities"""
        if self.used_quantity < 0:
            raise ValueError("Used quantity cannot be negative")
        if self.used_quantity > self.initial_quantity:
            raise ValueError(f"Used quantity ({self.used_quantity}) exceeds initial quantity ({self.initial_quantity})")
    
    def calculate_quantities(self):
        """Calculate remaining quantity and total cost"""
        self.remaining_quantity = self.initial_quantity - self.used_quantity
        self.total_cost = self.used_quantity * self.price_per_kg

@dataclass
class Expense:
    """Expense class for tracking all farm expenses"""
    category: ExpenseCategory
    description: str
    amount: float
    date: datetime = field(default_factory=datetime.now)
    unit: str = "USD"

@dataclass
class ChickenBatch:
    """Represents a batch of chickens"""
    batch_id: str
    purchase_date: datetime
    initial_count: int
    mortality_rate: float = 0.0
    mortality_count: int = field(init=False)
    surviving_count: int = field(init=False)
    
    def __post_init__(self):
        self.calculate_mortality()
    
    def calculate_mortality(self):
        """Calculate mortality and surviving chickens"""
        self.mortality_count = int(self.initial_count * (self.mortality_rate / 100))
        self.surviving_count = self.initial_count - self.mortality_count

# ========== MAIN FARM CLASS ==========

class PoultryFarm:
    """Main class representing the poultry farm with all operations"""
    
    def __init__(self, name: str = "My Poultry Farm"):
        self.name = name
        self.initial_capital = 0.0
        self.current_capital = 0.0
        self.chicken_batch: Optional[ChickenBatch] = None
        self.feeds: Dict[FeedType, Feed] = {}
        self.expenses: List[Expense] = []
        self.sales_income = 0.0
        self.sales_count = 0
        self.performance_metrics: Dict[str, float] = {}
        self.created_at = datetime.now()
    
    def _validate_positive_float(self, value: float, field_name: str) -> float:
        """Validate that a float value is positive"""
        if value < 0:
            raise ValueError(f"{field_name} cannot be negative")
        return value
    
    def _validate_positive_int(self, value: int, field_name: str) -> int:
        """Validate that an integer value is positive"""
        if value < 0:
            raise ValueError(f"{field_name} cannot be negative")
        return value
    
    def set_initial_capital(self, capital: float):
        """Set initial capital for the farm"""
        self.initial_capital = self._validate_positive_float(capital, "Initial capital")
        self.current_capital = self.initial_capital
    
    def purchase_chicks(self, count: int, price_per_chick: float) -> float:
        """Purchase day-old chicks"""
        count = self._validate_positive_int(count, "Chick count")
        price_per_chick = self._validate_positive_float(price_per_chick, "Price per chick")
        
        total_cost = count * price_per_chick
        if total_cost > self.current_capital:
            raise ValueError(f"Insufficient capital. Need ${total_cost:.2f}, have ${self.current_capital:.2f}")
        
        # Create chicken batch
        batch_id = f"BATCH-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self.chicken_batch = ChickenBatch(
            batch_id=batch_id,
            purchase_date=datetime.now(),
            initial_count=count
        )
        
        # Record expense
        self.expenses.append(Expense(
            category=ExpenseCategory.CAPITAL,
            description=f"Purchase of {count} day-old chicks",
            amount=total_cost
        ))
        
        self.current_capital -= total_cost
        return total_cost
    
    def set_mortality_rate(self, mortality_rate: float):
        """Set mortality rate for the current chicken batch"""
        if not self.chicken_batch:
            raise ValueError("No chicken batch purchased yet")
        
        self.chicken_batch.mortality_rate = self._validate_positive_float(
            mortality_rate, "Mortality rate"
        )
        self.chicken_batch.calculate_mortality()
    
    @lru_cache(maxsize=3)  # Cache feed calculations for better performance
    def manage_feed(self, feed_type: FeedType, initial_qty: float, used_qty: float, price_per_kg: float) -> Feed:
        """Manage feed for a specific type"""
        initial_qty = self._validate_positive_float(initial_qty, "Initial quantity")
        used_qty = self._validate_positive_float(used_qty, "Used quantity")
        price_per_kg = self._validate_positive_float(price_per_kg, "Price per kg")
        
        feed = Feed(
            feed_type=feed_type,
            initial_quantity=initial_qty,
            used_quantity=used_qty,
            price_per_kg=price_per_kg
        )
        
        self.feeds[feed_type] = feed
        self.current_capital -= feed.total_cost
        
        self.expenses.append(Expense(
            category=ExpenseCategory.FEED,
            description=f"{feed_type.value.capitalize()} feed",
            amount=feed.total_cost
        ))
        
        return feed
    
    def record_electricity_cost(self, units_used: float, cost_per_kwh: float = 0.98):
        """Record electricity expense"""
        units_used = self._validate_positive_float(units_used, "Electricity units")
        cost_per_kwh = self._validate_positive_float(cost_per_kwh, "Cost per kWh")
        
        electricity_cost = units_used * cost_per_kwh
        self.current_capital -= electricity_cost
        
        self.expenses.append(Expense(
            category=ExpenseCategory.UTILITIES,
            description=f"Electricity ({units_used} kWh)",
            amount=electricity_cost
        ))
        
        return electricity_cost
    
    def record_medical_expenses(self, vaccination_cost: float, medication_cost: float):
        """Record medical and veterinary expenses"""
        vaccination_cost = self._validate_positive_float(vaccination_cost, "Vaccination cost")
        medication_cost = self._validate_positive_float(medication_cost, "Medication cost")
        
        total_medical = vaccination_cost + medication_cost
        self.current_capital -= total_medical
        
        self.expenses.append(Expense(
            category=ExpenseCategory.MEDICAL,
            description="Vaccination",
            amount=vaccination_cost
        ))
        
        self.expenses.append(Expense(
            category=ExpenseCategory.MEDICAL,
            description="Medication",
            amount=medication_cost
        ))
        
        return total_medical
    
    def record_labor_cost(self, labor_hours: float, hourly_rate: float):
        """Record labor costs"""
        labor_hours = self._validate_positive_float(labor_hours, "Labor hours")
        hourly_rate = self._validate_positive_float(hourly_rate, "Hourly rate")
        
        labor_cost = labor_hours * hourly_rate
        self.current_capital -= labor_cost
        
        self.expenses.append(Expense(
            category=ExpenseCategory.LABOR,
            description=f"Labor ({labor_hours} hours)",
            amount=labor_cost
        ))
        
        return labor_cost
    
    def record_sales(self, chickens_sold: int, selling_price: float):
        """Record chicken sales"""
        if not self.chicken_batch:
            raise ValueError("No chickens available for sale")
        
        chickens_sold = self._validate_positive_int(chickens_sold, "Chickens sold")
        selling_price = self._validate_positive_float(selling_price, "Selling price")
        
        if chickens_sold > self.chicken_batch.surviving_count:
            raise ValueError(f"Cannot sell {chickens_sold} chickens. Only {self.chicken_batch.surviving_count} available")
        
        self.sales_count = chickens_sold
        self.sales_income = chickens_sold * selling_price
        self.current_capital += self.sales_income
        
        return self.sales_income
    
    def calculate_performance_metrics(self):
        """Calculate various performance metrics"""
        if not self.chicken_batch or self.sales_count == 0:
            return
        
        total_expenses = sum(expense.amount for expense in self.expenses)
        net_profit = self.current_capital - self.initial_capital
        
        # Use numpy for faster calculations
        expenses_array = np.array([expense.amount for expense in self.expenses])
        total_expenses = np.sum(expenses_array)
        
        self.performance_metrics = {
            'total_expenses': total_expenses,
            'net_profit': net_profit,
            'net_loss': abs(net_profit) if net_profit < 0 else 0,
            'cost_per_chicken': total_expenses / self.sales_count,
            'profit_per_chicken': net_profit / self.sales_count,
            'break_even_price': total_expenses / self.sales_count,
            'return_on_investment': (net_profit / total_expenses * 100) if total_expenses > 0 else 0,
            'mortality_rate': self.chicken_batch.mortality_rate,
            'capital_efficiency': (self.current_capital / self.initial_capital * 100) if self.initial_capital > 0 else 0
        }
        
        # Calculate feed conversion ratio if feed data exists
        if FeedType.STARTER in self.feeds:
            total_feed_cost = sum(feed.total_cost for feed in self.feeds.values())
            self.performance_metrics['feed_conversion_ratio'] = total_feed_cost / self.sales_count
    
    def generate_report(self) -> str:
        """Generate comprehensive farm report"""
        self.calculate_performance_metrics()
        
        report_lines = []
        report_lines.append("=" * 60)
        report_lines.append(f"POULTRY FARM MANAGEMENT & PROFIT SYSTEM")
        report_lines.append(f"Farm: {self.name}")
        report_lines.append(f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("=" * 60)
        
        # Financial Summary
        report_lines.append("\nFINANCIAL SUMMARY")
        report_lines.append("-" * 40)
        report_lines.append(f"Initial Capital      : ${self.initial_capital:,.2f}")
        report_lines.append(f"Final Capital        : ${self.current_capital:,.2f}")
        report_lines.append(f"Sales Income         : ${self.sales_income:,.2f}")
        
        # Expenses Breakdown
        report_lines.append("\nEXPENSES BREAKDOWN")
        report_lines.append("-" * 40)
        expenses_by_category = defaultdict(float)
        for expense in self.expenses:
            expenses_by_category[expense.category.value] += expense.amount
        
        for category, amount in expenses_by_category.items():
            report_lines.append(f"{category:<20}: ${amount:,.2f}")
        
        # Performance Metrics
        report_lines.append("\nPERFORMANCE METRICS")
        report_lines.append("-" * 40)
        for metric, value in self.performance_metrics.items():
            metric_name = metric.replace('_', ' ').title()
            if 'percent' in metric or 'rate' in metric or 'roi' in metric.lower():
                report_lines.append(f"{metric_name:<25}: {value:.2f}%")
            else:
                report_lines.append(f"{metric_name:<25}: ${value:,.2f}")
        
        # Chicken Information
        if self.chicken_batch:
            report_lines.append("\nCHICKEN BATCH INFORMATION")
            report_lines.append("-" * 40)
            report_lines.append(f"Batch ID             : {self.chicken_batch.batch_id}")
            report_lines.append(f"Initial Count        : {self.chicken_batch.initial_count}")
            report_lines.append(f"Mortality Count      : {self.chicken_batch.mortality_count}")
            report_lines.append(f"Surviving Count      : {self.chicken_batch.surviving_count}")
            report_lines.append(f"Chickens Sold        : {self.sales_count}")
        
        # Final Status
        report_lines.append("\n" + "=" * 60)
        profit_status = "PROFIT" if self.performance_metrics.get('net_profit', 0) >= 0 else "LOSS"
        report_lines.append(f"FINAL STATUS: {profit_status}")
        report_lines.append("=" * 60)
        
        return "\n".join(report_lines)
    
    def save_report_to_file(self, filename: str = None):
        """Save report to file in multiple formats"""
        if filename is None:
            filename = f"farm_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        report = self.generate_report()
        
        # Save as text file
        with open(f"{filename}.txt", 'w') as f:
            f.write(report)
        
        # Save as JSON for data interchange
        data = {
            'farm_name': self.name,
            'initial_capital': self.initial_capital,
            'current_capital': self.current_capital,
            'sales_income': self.sales_income,
            'expenses': [{'category': exp.category.value, 'description': exp.description, 'amount': exp.amount} 
                        for exp in self.expenses],
            'performance_metrics': self.performance_metrics,
            'report_date': datetime.now().isoformat()
        }
        
        with open(f"{filename}.json", 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        # Save as pickle for Python object serialization
        with open(f"{filename}.pkl", 'wb') as f:
            pickle.dump(self, f)
        
        print(f"\nReport saved to {filename}.txt, {filename}.json, and {filename}.pkl")
    
    def to_dict(self) -> Dict:
        """Convert farm data to dictionary for serialization"""
        return {
            'name': self.name,
            'initial_capital': self.initial_capital,
            'current_capital': self.current_capital,
            'sales_income': self.sales_income,
            'sales_count': self.sales_count,
            'chicken_batch': {
                'batch_id': self.chicken_batch.batch_id if self.chicken_batch else None,
                'initial_count': self.chicken_batch.initial_count if self.chicken_batch else 0,
                'mortality_rate': self.chicken_batch.mortality_rate if self.chicken_batch else 0,
                'mortality_count': self.chicken_batch.mortality_count if self.chicken_batch else 0,
                'surviving_count': self.chicken_batch.surviving_count if self.chicken_batch else 0,
            } if self.chicken_batch else None,
            'expenses': [{
                'category': exp.category.value,
                'description': exp.description,
                'amount': exp.amount,
                'date': exp.date.isoformat()
            } for exp in self.expenses],
            'feeds': {feed_type.value: {
                'initial_quantity': feed.initial_quantity,
                'used_quantity': feed.used_quantity,
                'price_per_kg': feed.price_per_kg,
                'total_cost': feed.total_cost,
                'remaining_quantity': feed.remaining_quantity
            } for feed_type, feed in self.feeds.items()},
            'performance_metrics': self.performance_metrics,
            'created_at': self.created_at.isoformat()
        }

# ========== FAST INPUT VALIDATION FUNCTIONS ==========

def get_valid_float(prompt: str, min_val: float = 0.0) -> float:
    """Get validated float input with error handling"""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_int(prompt: str, min_val: int = 0) -> int:
    """Get validated integer input with error handling"""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# ========== MAIN EXECUTION WITH PERFORMANCE TRACKING ==========

def main():
    """Main execution function"""
    
    # Performance tracking
    start_time = time.time()
    
    print("\n" + "=" * 60)
    print(" POULTRY FARM MANAGEMENT & PROFIT SYSTEM ")
    print("=" * 60 + "\n")
    
    # Create farm instance
    farm_name = input("Enter farm name: ").strip() or "My Poultry Farm"
    farm = PoultryFarm(farm_name)
    
    try:
        # ---------- CAPITAL & CHICK PURCHASE ----------
        print("\n===== CAPITAL & CHICK PURCHASE =====")
        initial_capital = get_valid_float("Enter initial capital (USD): ")
        farm.set_initial_capital(initial_capital)
        
        day_old_chicks = get_valid_int("Enter number of day-old chicks bought: ")
        price_per_chick = get_valid_float("Enter price per day-old chick (USD): ")
        
        chicks_cost = farm.purchase_chicks(day_old_chicks, price_per_chick)
        print(f"\n✓ Purchased {day_old_chicks} chicks for ${chicks_cost:.2f}")
        print(f"  Remaining capital: ${farm.current_capital:.2f}")
        
        # ---------- MORTALITY TRACKING ----------
        print("\n===== MORTALITY TRACKING =====")
        mortality_rate = get_valid_float("Enter mortality rate (as percentage, e.g., 5 for 5%): ", 0.0)
        farm.set_mortality_rate(mortality_rate)
        
        if farm.chicken_batch:
            print(f"\n✓ Mortality Tracking:")
            print(f"  Initial chickens: {farm.chicken_batch.initial_count}")
            print(f"  Mortality rate: {farm.chicken_batch.mortality_rate:.1f}%")
            print(f"  Chickens lost: {farm.chicken_batch.mortality_count}")
            print(f"  Surviving chickens: {farm.chicken_batch.surviving_count}")
        
        # ---------- FEED MANAGEMENT ----------
        print("\n===== FEED MANAGEMENT =====")
        
        for feed_type in FeedType:
            print(f"\n--- {feed_type.value.upper()} FEED ---")
            initial_qty = get_valid_float(f"Enter initial {feed_type.value} feed quantity (kg): ")
            used_qty = get_valid_float(f"Enter used {feed_type.value} feed quantity (kg): ")
            price_per_kg = get_valid_float(f"Enter {feed_type.value} feed price per kg (USD): ")
            
            feed = farm.manage_feed(feed_type, initial_qty, used_qty, price_per_kg)
            print(f"✓ {feed_type.value.capitalize()} feed cost: ${feed.total_cost:.2f}")
            print(f"  Remaining {feed_type.value} feed: {feed.remaining_quantity:.2f} kg")
        
        print(f"\n✓ Remaining capital after feed: ${farm.current_capital:.2f}")
        
        # ---------- ELECTRICITY EXPENSE ----------
        print("\n===== ELECTRICITY EXPENSE =====")
        units_used = get_valid_float("Enter electricity units used (kWh): ")
        electricity_cost = farm.record_electricity_cost(units_used)
        print(f"✓ Electricity cost: ${electricity_cost:.2f}")
        print(f"  Remaining capital after electricity: ${farm.current_capital:.2f}")
        
        # ---------- MEDICAL EXPENSES ----------
        print("\n===== MEDICAL & VETERINARY EXPENSES =====")
        vaccination_cost = get_valid_float("Enter vaccination costs (USD): ")
        medication_cost = get_valid_float("Enter medication costs (USD): ")
        medical_cost = farm.record_medical_expenses(vaccination_cost, medication_cost)
        print(f"✓ Total medical expenses: ${medical_cost:.2f}")
        print(f"  Remaining capital after medical: ${farm.current_capital:.2f}")
        
        # ---------- LABOR COSTS ----------
        print("\n===== LABOR COSTS =====")
        labor_hours = get_valid_float("Enter total labor hours: ")
        hourly_rate = get_valid_float("Enter hourly labor rate (USD): ")
        labor_cost = farm.record_labor_cost(labor_hours, hourly_rate)
        print(f"✓ Labor cost: ${labor_cost:.2f}")
        print(f"  Remaining capital after labor: ${farm.current_capital:.2f}")
        
        # ---------- SALES ----------
        print("\n===== SALES =====")
        if farm.chicken_batch:
            max_sellable = farm.chicken_batch.surviving_count
            chickens_sold = get_valid_int(
                f"Enter number of chickens to sell (max {max_sellable}): ", 
                0
            )
            
            if chickens_sold > max_sellable:
                print(f"Warning: Cannot sell more than {max_sellable} chickens. Adjusting to maximum.")
                chickens_sold = max_sellable
            
            selling_price = get_valid_float("Enter selling price per chicken (USD): ")
            sales_income = farm.record_sales(chickens_sold, selling_price)
            print(f"\n✓ Sold {chickens_sold} chickens for ${sales_income:.2f}")
            print(f"  Final capital: ${farm.current_capital:.2f}")
            
            if chickens_sold < max_sellable:
                remaining_chickens = max_sellable - chickens_sold
                print(f"  Note: {remaining_chickens} chickens remain unsold")
        else:
            print("No chickens available for sale.")
        
        # ---------- GENERATE REPORT ----------
        print("\n" + "=" * 60)
        print(" GENERATING COMPREHENSIVE REPORT ")
        print("=" * 60)
        
        report = farm.generate_report()
        print(report)
        
        # ---------- SAVE REPORT ----------
        save_option = input("\nDo you want to save the report? (yes/no): ").strip().lower()
        if save_option in ['yes', 'y']:
            filename = input("Enter filename (without extension): ").strip()
            farm.save_report_to_file(filename)
        
        # ---------- PERFORMANCE STATISTICS ----------
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"\n" + "=" * 60)
        print(" PERFORMANCE STATISTICS ")
        print("=" * 60)
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Total expenses recorded: {len(farm.expenses)}")
        print(f"Memory usage optimized with caching")
        print("=" * 60)
        
        # ---------- OPTIONAL: DISPLAY AS NUMPY ARRAY ----------
        if farm.expenses:
            print("\nExpense Breakdown (Numpy Array):")
            expense_categories = [exp.category.value for exp in farm.expenses]
            expense_amounts = [exp.amount for exp in farm.expenses]
            
            # Use numpy for statistical analysis
            amounts_array = np.array(expense_amounts)
            print(f"Mean expense: ${np.mean(amounts_array):.2f}")
            print(f"Max expense: ${np.max(amounts_array):.2f}")
            print(f"Min expense: ${np.min(amounts_array):.2f}")
            print(f"Total expenses (numpy sum): ${np.sum(amounts_array):.2f}")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("Please restart the program and enter valid data.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    finally:
        print("\n" + "=" * 60)
        print(" SYSTEM EXECUTION COMPLETED ")
        print("=" * 60)

# ========== ADDITIONAL UTILITY FUNCTIONS ==========

def load_farm_from_file(filename: str) -> Optional[PoultryFarm]:
    """Load a saved farm object from pickle file"""
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def export_to_csv(farm: PoultryFarm, filename: str):
    """Export farm data to CSV format"""
    data = farm.to_dict()
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(['Category', 'Description', 'Amount', 'Date'])
        
        # Write expenses
        for expense in data['expenses']:
            writer.writerow([
                expense['category'],
                expense['description'],
                expense['amount'],
                expense['date']
            ])
    
    print(f"Data exported to {filename}")

# ========== RUN MAIN PROGRAM ==========

if __name__ == "__main__":
    # Check for command line arguments
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--load":
        if len(sys.argv) > 2:
            farm = load_farm_from_file(sys.argv[2])
            if farm:
                print(farm.generate_report())
        else:
            print("Please specify a filename to load.")
    else:
        main()