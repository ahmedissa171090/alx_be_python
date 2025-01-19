# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance (default is 0)."""
        self._account_balance = initial_balance  # Encapsulated account balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds exist."""
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        elif amount > 0:
            return False  # Return False for insufficient funds
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current Balance: ${self._account_balance:.2f}")
