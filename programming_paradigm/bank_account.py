class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance"""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add funds to the account"""
        if amount > 0:
            self.account_balance += amount
        # No print, main-0.py handles output

    def withdraw(self, amount):
        """Withdraw funds if balance is sufficient"""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Return the current balance"""
        return self.account_balance
