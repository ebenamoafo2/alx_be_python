class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add funds to the account"""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw funds if balance is sufficient"""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew {amount}.")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Show the current account balance"""
        print(f"Current balance: {self.account_balance}")
