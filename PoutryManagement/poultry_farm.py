import os

# ---------- SAFE INPUT FUNCTIONS ----------
def safe_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def safe_int(prompt): 
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


# ---------- POULTRY FARM CLASS ----------
class PoultryFarm:
    #----------constructor----------
    def __init__(self, farm_name, initial_capital):
        self.farm_name = farm_name.upper()
        self.initial_capital = initial_capital
        self.money_available = initial_capital

        self.day_old_chicks = 0
        self.chicks_cost = 0

        self.total_feed_cost = 0
        self.electricity_cost = 0
        self.total_labor_cost = 0
        self.medical_cost = 0
        self.vaccine_cost = 0

        self.chickens_sold = 0
        self.available_chicken = 0
        self.sales_income = 0

    # ---------- CHICK PURCHASE ----------
    def buy_chicks(self):
        print("\n===== CAPITAL & CHICKS MANAGEMENT =====\n")
        self.day_old_chicks = safe_int("Enter number of day-old chicks bought: ")
        price_per_chick = safe_float("Enter price per day-old chick (USD): ")

        self.chicks_cost = self.day_old_chicks * price_per_chick
        self.money_available -= self.chicks_cost

        print(f"\nCost of chicks: ${self.chicks_cost:.2f}")
        print(f"Remaining capital: ${self.money_available:.2f}")

    # ---------- FEED MANAGEMENT ----------
    def feed_cost(self, feed_name):
        print(f"\n--- {feed_name.upper()} FEED ---")
        initial_qty = safe_float(f"Enter initial {feed_name} feed quantity (kg): ")
        used_qty = safe_float(f"Enter used {feed_name} feed quantity (kg): ")

        if used_qty > initial_qty:
            print("Error: Used feed cannot exceed available feed.")
            return 0

        price_per_kg = safe_float(f"Enter {feed_name} feed price per kg (USD): ")
        cost = used_qty * price_per_kg

        # STORE VALUES FOR REPORT
        setattr(self, f"{feed_name}_initial", initial_qty)
        setattr(self, f"{feed_name}_used", used_qty)
        setattr(self, f"{feed_name}_remaining", initial_qty - used_qty)

        print(f"{feed_name.capitalize()} feed cost: ${cost:.2f}")
        return cost


    def manage_feed(self):
        print("\n===== FEED MANAGEMENT =====")
        self.total_feed_cost = (
            self.feed_cost("starter")
            + self.feed_cost("grower")
            + self.feed_cost("finisher")
        )
        self.money_available -= self.total_feed_cost
        print(f"Remaining capital: ${self.money_available:.2f}")

    # ---------- ELECTRICITY ----------
    def electricity_expense(self):
        print("\n===== ELECTRICITY ===========")
        units = safe_float("Enter electricity units used (kWh): ")
        self.electricity_cost = units * 0.98
        self.money_available -= self.electricity_cost

    # ---------- LABOUR ----------
    def labour_expense(self):
        print("\n===== LABOUR MANAGEMENT =========")
        workers = safe_int("Enter number of workers: ")
        hours = safe_int("Enter number of worked hours: ")
        rate = safe_float("Enter labour cost per hour (USD): ")

        self.total_labor_cost = workers * hours * rate
        self.money_available -= self.total_labor_cost
        print(f"Remaining capital: ${self.money_available:.2f}")

    # ---------- MEDICAL ----------
    def medical_expense(self):
        print("\n===== MEDIACAL COST MANAGEMENT MODULE =====")
        self.medical_cost = safe_float("Enter medical cost (USD): ")
        self.vaccine_cost = safe_float("Enter vaccination cost (USD): ")
        self.money_available -= (self.medical_cost + self.vaccine_cost)
        print(f"Remaining capital: ${self.money_available:.2f}")

    # ---------- SALES ----------
    def sales(self):
        print("\n===== SALES MANAGEMENT ==========")
        self.chickens_sold = safe_int("Enter number of chickens sold: ")
        price = safe_float("Enter selling price per chicken (USD): ")
        self.available_chicken = safe_int("Enter number of unsold chickens: ")

        self.sales_income = self.chickens_sold * price
        self.money_available += self.sales_income
        print(f"Final capital: ${self.money_available:.2f}")

    # ---------- CALCULATIONS ----------
    def mortality_rate(self):
        dead = self.day_old_chicks - (self.chickens_sold + self.available_chicken)
        return (dead / self.day_old_chicks) * 100 if self.day_old_chicks else 0

    def total_expenses(self):
        return (
            self.chicks_cost
            + self.total_feed_cost
            + self.electricity_cost
            + self.total_labor_cost
            + self.medical_cost
            + self.vaccine_cost
        )

    def net_profit(self):
        return self.money_available - self.initial_capital

    # ---------- REPORT ----------
    def generate_report(self):
        os.system("cls" if os.name == "nt" else "clear")

        print(f"""
==================================================
        {self.farm_name} POULTRY FARM REPORT
==================================================""")

        print(f"Initial Capital              : ${self.initial_capital:.2f}")
        print(f"Total Expenses               : ${self.total_expenses():.2f}")
        print(f"Starter Feed Remaining (kg)  : {getattr(self, 'starter_remaining', 0):.2f}")
        print(f"Grower Feed Remaining (kg)   : {getattr(self, 'grower_remaining', 0):.2f}")
        print(f"Finisher Feed Remaining (kg) : {getattr(self, 'finisher_remaining', 0):.2f}")
        print(f"Final Capital                : ${self.money_available:.2f}")
        print(f"Mortality Rate               : {self.mortality_rate():.2f}%")

        profit = self.net_profit()
        if profit >= 0:
            print(f"\nNET PROFIT : ${profit:.2f}")
            print("FINAL STATUS :YOU MADE  PROFIT — BUSINESS DOING GREAT")
        else:
            print(f"\nNET LOSS   : ${abs(profit):.2f}")
            print("FINAL STATUS : YOU HAVE A LOSS — REVIEW STRATEGY")


# ---------- MAIN PROGRAM ----------
print("\n==============================================")
print(" POULTRY FARM MANAGEMENT & PROFIT SYSTEM ")
print("==============================================\n")



print("""
==================================================
        GREENFIELD POULTRY FARM REPORT
==================================================
Initial Capital              : $5000.00
Total Expenses               : $3120.50
Starter Feed Remaining (kg)  : 120.00
Grower Feed Remaining (kg)   : 95.00
Finisher Feed Remaining (kg) : 40.00
Sales Income                 : $4200.00
Final Capital                : $6079.50
Mortality Rate               : 4.25%

NET PROFIT : $1079.50
FINAL STATUS : PROFIT — BUSINESS DOING GREAT \n""")

farm_name = input("Enter farm name: ")
initial_capital = safe_float("Enter initial capital (USD): ")

farm = PoultryFarm(farm_name, initial_capital)

farm.buy_chicks()
farm.manage_feed()
farm.electricity_expense()
farm.labour_expense()
farm.medical_expense()
farm.sales()
farm.generate_report()

# A project min poulty farm project developed by GOROGODO TAKUNDA LEONARD to help farm manage his business in a proffessional manner 