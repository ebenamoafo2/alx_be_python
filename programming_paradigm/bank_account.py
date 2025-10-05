class BankAccount:
    """A simple bank account class for managing deposits and withdrawals."""

    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional initial balance.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")