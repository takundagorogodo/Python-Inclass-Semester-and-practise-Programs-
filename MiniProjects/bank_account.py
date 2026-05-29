class BankAccount:
      def __init__(self, account_holder_name, balance):
            self.account_holder_name = account_holder_name
            self.amount = balance

      def deposit(self, money_top):
            if money_top <= 0:
                  print("Deposit amount must be positive")
            else:
                  self.amount += money_top
                  print(f"You added {money_top}. New account balance is ${self.amount}")

      def withdraw(self, money_deduct):
            if money_deduct <= 0:
                  print("Withdrawal amount must be positive")
            elif money_deduct > self.amount:
                  print("Insufficient balance")
            else:
                  self.amount -= money_deduct
                  print(f"You withdrew {money_deduct}. Account balance is ${self.amount}")


a_1 = BankAccount("Takunda", 90)
a_1.deposit(10)
a_1.withdraw(200)
a_1.deposit(1000)

#
#
#class BankAccount:
#      def __init__(self, account_number, account_holder_name, balance=0):
#            self.account_number = account_number
#            self.account_holder_name = account_holder_name
#            self.balance = balance
#            self.transactions = []
#
#      def deposit(self, amount):
#            if amount <= 0:
#                  print("Deposit amount must be positive")
#                  return
#            self.balance += amount
#            self.transactions.append(f"Deposited: {amount}")
#            print(f"Deposited {amount}. Balance: {self.balance}")
#
#      def withdraw(self, amount):
#            if amount <= 0:
#                  print("Withdrawal amount must be positive")
#                  return
#            if amount > self.balance:
#                  print("Insufficient balance")
#                  return
#            self.balance -= amount
#            self.transactions.append(f"Withdrew: {amount}")
#            print(f"Withdrew {amount}. Balance: {self.balance}")
#
#      def show_balance(self):
#            print(f"Account Balance: {self.balance}")
#
#      def show_transactions(self):
#            print("Transaction History:")
#            for t in self.transactions:
#                  print("-", t)
#
#
#class Bank:
#      def __init__(self):
#            self.accounts = {}
#
#      def create_account(self, account_number, name, balance=0):
#            if account_number in self.accounts:
#                  print("Account already exists")
#                  return
#            self.accounts[account_number] = BankAccount(account_number, name, balance)
#            print("Account created successfully")
#
#      def get_account(self, account_number):
#            return self.accounts.get(account_number, None)
#
#
## ----------- USING THE BANK SYSTEM -----------
#
#bank = Bank()
#
#bank.create_account(101, "Takunda", 90)
#bank.create_account(102, "Prosperity", 200)
#
#acc1 = bank.get_account(101)
#acc2 = bank.get_account(102)
#
#acc1.deposit(50)
#acc1.withdraw(30)
#acc1.withdraw(200)
#
#acc1.show_balance()
#acc1.show_transactions()
