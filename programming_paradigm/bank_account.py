class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulating the account balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds exist."""
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        elif amount > 0:
            print("Insufficient funds.")
            return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
