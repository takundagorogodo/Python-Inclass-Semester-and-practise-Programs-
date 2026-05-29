"""
Banking System - A professional banking simulation module.
Implements core banking operations with account management and transaction tracking.
"""

from typing import List, Optional, Dict
from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class Transaction:
    """Represents a financial transaction with metadata."""
    transaction_id: str
    type: str  # 'deposit' or 'withdrawal'
    amount: float
    timestamp: datetime
    status: str  # 'completed', 'failed'
    description: str = ""

    def __str__(self) -> str:
        """String representation of transaction."""
        return (f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | "
                f"{self.type.upper():10} | ${self.amount:10.2f} | "
                f"{self.status:10} | {self.description}")


class BankAccount:
    """Represents a bank account with transaction capabilities."""
    
    def __init__(self, account_number: str, account_holder_name: str, initial_balance: float = 0.0):
        """
        Initialize a new bank account.
        
        Args:
            account_number: Unique account identifier
            account_holder_name: Name of the account holder
            initial_balance: Starting balance (default: 0)
            
        Raises:
            ValueError: If initial_balance is negative
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
            
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self._balance = initial_balance
        self.transactions: List[Transaction] = []
        self.is_active = True
        self.created_at = datetime.now()
        
        # Record initial deposit if balance > 0
        if initial_balance > 0:
            initial_tx = Transaction(
                transaction_id=str(uuid.uuid4()),
                type="deposit",
                amount=initial_balance,
                timestamp=self.created_at,
                status="completed",
                description="Initial deposit"
            )
            self.transactions.append(initial_tx)
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Returns:
            bool: True if successful, False otherwise
            
        Raises:
            ValueError: If account is inactive
        """
        if not self.is_active:
            raise ValueError("Cannot perform operations on inactive account")
            
        if amount <= 0:
            print(f"❌ Deposit failed: Amount must be positive (attempted: ${amount:.2f})")
            self._record_transaction("deposit", amount, "failed", 
                                   "Amount must be positive")
            return False
            
        self._balance += amount
        print(f"✅ Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        self._record_transaction("deposit", amount, "completed")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw (must be positive)
            
        Returns:
            bool: True if successful, False otherwise
            
        Raises:
            ValueError: If account is inactive
        """
        if not self.is_active:
            raise ValueError("Cannot perform operations on inactive account")
            
        if amount <= 0:
            print(f"❌ Withdrawal failed: Amount must be positive (attempted: ${amount:.2f})")
            self._record_transaction("withdrawal", amount, "failed", 
                                   "Amount must be positive")
            return False
            
        if amount > self._balance:
            print(f"❌ Withdrawal failed: Insufficient funds. "
                  f"Balance: ${self._balance:.2f}, Attempted: ${amount:.2f}")
            self._record_transaction("withdrawal", amount, "failed", 
                                   "Insufficient funds")
            return False
            
        self._balance -= amount
        print(f"✅ Withdrew ${amount:.2f}. Remaining balance: ${self._balance:.2f}")
        self._record_transaction("withdrawal", amount, "completed")
        return True
    
    def transfer(self, amount: float, recipient: 'BankAccount') -> bool:
        """
        Transfer money to another account.
        
        Args:
            amount: Amount to transfer
            recipient: Destination BankAccount object
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.is_active or not recipient.is_active:
            print("❌ Transfer failed: One or both accounts are inactive")
            return False
            
        if self.withdraw(amount):
            if recipient.deposit(amount):
                # Record transfer-specific transaction
                tx_id = str(uuid.uuid4())
                self._record_transaction("transfer_out", amount, "completed",
                                       f"To: {recipient.account_number}")
                recipient._record_transaction("transfer_in", amount, "completed",
                                            f"From: {self.account_number}")
                print(f"✅ Transfer successful: ${amount:.2f} to account {recipient.account_number}")
                return True
            else:
                # Refund if deposit fails
                self._balance += amount
                print("❌ Transfer failed: Recipient deposit unsuccessful")
        return False
    
    def get_balance(self) -> float:
        """Get current account balance."""
        return self._balance
    
    def get_statement(self, limit: Optional[int] = None) -> List[Transaction]:
        """
        Get account statement with recent transactions.
        
        Args:
            limit: Maximum number of transactions to return (None for all)
            
        Returns:
            List of Transaction objects
        """
        if limit:
            return self.transactions[-limit:]
        return self.transactions.copy()
    
    def print_statement(self, limit: int = 10) -> None:
        """Print formatted account statement."""
        print(f"\n{'='*60}")
        print(f"ACCOUNT STATEMENT")
        print(f"{'='*60}")
        print(f"Account: {self.account_number}")
        print(f"Holder: {self.account_holder_name}")
        print(f"Current Balance: ${self._balance:.2f}")
        print(f"Status: {'Active' if self.is_active else 'Inactive'}")
        print(f"{'='*60}")
        print(f"RECENT TRANSACTIONS")
        print(f"{'='*60}")
        
        if not self.transactions:
            print("No transactions found.")
            return
            
        # Header
        print(f"{'Date/Time':20} | {'Type':10} | {'Amount':12} | {'Status':10} | Description")
        print(f"{'-'*20}-|-{'-'*10}-|-{'-'*12}-|-{'-'*10}-|-{'-'*20}")
        
        # Print transactions (most recent first)
        for tx in reversed(self.get_statement(limit)):
            print(tx)
    
    def deactivate(self) -> None:
        """Deactivate the account."""
        if self._balance > 0:
            print(f"⚠️  Account has balance of ${self._balance:.2f}. "
                  f"Withdraw funds before deactivation.")
            return
        self.is_active = False
        print(f"Account {self.account_number} deactivated.")
    
    def _record_transaction(self, tx_type: str, amount: float, 
                          status: str, description: str = "") -> None:
        """Helper method to record transactions."""
        transaction = Transaction(
            transaction_id=str(uuid.uuid4()),
            type=tx_type,
            amount=amount,
            timestamp=datetime.now(),
            status=status,
            description=description
        )
        self.transactions.append(transaction)
    
    def __str__(self) -> str:
        """String representation of the account."""
        status = "Active" if self.is_active else "Inactive"
        return (f"Account: {self.account_number} | "
                f"Holder: {self.account_holder_name} | "
                f"Balance: ${self._balance:.2f} | "
                f"Status: {status}")


class Bank:
    """Manages multiple bank accounts and banking operations."""
    
    def __init__(self, name: str = "TrustBank"):
        """
        Initialize a new bank.
        
        Args:
            name: Bank name
        """
        self.name = name
        self.accounts: Dict[str, BankAccount] = {}
        self._next_account_number = 1001
    
    def create_account(self, account_holder_name: str, 
                      initial_deposit: float = 0.0) -> BankAccount:
        """
        Create a new bank account with automatic account number generation.
        
        Args:
            account_holder_name: Name of the account holder
            initial_deposit: Initial deposit amount (default: 0)
            
        Returns:
            Newly created BankAccount object
            
        Raises:
            ValueError: If initial_deposit is negative
        """
        account_number = str(self._next_account_number)
        self._next_account_number += 1
        
        account = BankAccount(account_number, account_holder_name, initial_deposit)
        self.accounts[account_number] = account
        
        print(f"\n✅ Account created successfully!")
        print(f"   Account Number: {account_number}")
        print(f"   Account Holder: {account_holder_name}")
        print(f"   Initial Balance: ${initial_deposit:.2f}")
        
        return account
    
    def get_account(self, account_number: str) -> Optional[BankAccount]:
        """
        Retrieve an account by account number.
        
        Args:
            account_number: Account number to look up
            
        Returns:
            BankAccount object if found, None otherwise
        """
        return self.accounts.get(account_number)
    
    def close_account(self, account_number: str) -> bool:
        """
        Close a bank account.
        
        Args:
            account_number: Account number to close
            
        Returns:
            bool: True if successful, False otherwise
        """
        account = self.get_account(account_number)
        if not account:
            print(f"❌ Account {account_number} not found.")
            return False
        
        if account.get_balance() > 0:
            print(f"❌ Cannot close account with balance. "
                  f"Current balance: ${account.get_balance():.2f}")
            return False
        
        account.is_active = False
        del self.accounts[account_number]
        print(f"✅ Account {account_number} closed successfully.")
        return True
    
    def get_total_deposits(self) -> float:
        """Get total deposits across all accounts."""
        return sum(account.get_balance() for account in self.accounts.values())
    
    def list_accounts(self) -> None:
        """List all accounts in the bank."""
        if not self.accounts:
            print("No accounts found.")
            return
        
        print(f"\n{'='*60}")
        print(f"{self.name} - Account Summary")
        print(f"{'='*60}")
        print(f"Total Accounts: {len(self.accounts)}")
        print(f"Total Deposits: ${self.get_total_deposits():.2f}")
        print(f"{'='*60}")
        
        for account in self.accounts.values():
            print(f"  • {account}")
    
    def __str__(self) -> str:
        """String representation of the bank."""
        return f"{self.name} - {len(self.accounts)} accounts"


def main() -> None:
    """Example usage of the banking system."""
    print("="*60)
    print("BANKING SYSTEM DEMONSTRATION")
    print("="*60)
    
    # Create a bank
    bank = Bank("TrustBank International")
    
    # Create accounts
    print("\n1. Creating accounts...")
    account1 = bank.create_account("Takunda Chiremba", 500.00)
    account2 = bank.create_account("Prosperity Moyo", 1000.00)
    
    # Perform transactions
    print("\n2. Performing transactions...")
    account1.deposit(250.50)
    account1.withdraw(100.00)
    account1.withdraw(700.00)  # Should fail - insufficient funds
    
    # Transfer between accounts
    print("\n3. Transferring funds...")
    account1.transfer(150.00, account2)
    
    # Print statements
    print("\n4. Account statements...")
    account1.print_statement()
    account2.print_statement(limit=5)
    
    # List all accounts
    print("\n5. Bank overview...")
    bank.list_accounts()


if __name__ == "__main__":
    main()