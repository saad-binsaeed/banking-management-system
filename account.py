class BankAccount:

    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = float(balance)
        self.transactions = []

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        self.balance += amount

        self.transactions.append(
            f"Deposited Rs.{amount}"
        )

        print("Deposit successful.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount

        self.transactions.append(
            f"Withdrawn Rs.{amount}"
        )

        print("Withdrawal successful.")

    def show_balance(self):

        print(
            f"\nCurrent Balance: Rs.{self.balance}"
        )

    def show_transactions(self):

        print("\nTransaction History")

        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print(transaction)
