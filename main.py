from account import BankAccount
from storage import save_accounts
from storage import load_accounts


accounts = load_accounts()


def create_account():

    username = input(
        "Enter username: "
    )

    if username in accounts:

        print(
            "Account already exists."
        )

        return

    password = input(
        "Enter password: "
    )

    accounts[username] = (
        BankAccount(
            username,
            password
        )
    )

    print(
        "Account created successfully."
    )


def login():

    username = input(
        "Username: "
    )

    password = input(
        "Password: "
    )

    if (
        username in accounts
        and
        accounts[username].password
        == password
    ):

        print(
            "\nLogin successful."
        )

        return accounts[username]

    print(
        "\nInvalid credentials."
    )

    return None


def user_menu(account):

    while True:

        print(
            """
======== ACCOUNT MENU ========

1. Deposit
2. Withdraw
3. Check Balance
4. Transaction History
5. Logout
"""
        )

        choice = input(
            "Choose option: "
        )

        if choice == "1":

            try:

                amount = float(
                    input(
                        "Amount: "
                    )
                )

                account.deposit(amount)

            except ValueError:

                print(
                    "Enter valid number."
                )

        elif choice == "2":

            try:

                amount = float(
                    input(
                        "Amount: "
                    )
                )

                account.withdraw(amount)

            except ValueError:

                print(
                    "Enter valid number."
                )

        elif choice == "3":

            account.show_balance()

        elif choice == "4":

            account.show_transactions()

        elif choice == "5":

            save_accounts(accounts)

            print("Logged out.")

            break

        else:

            print("Invalid choice.")


while True:

    print(
        """
====== BANKING SYSTEM ======

1. Create Account
2. Login
3. Exit
"""
    )

    choice = input(
        "Select option: "
    )

    if choice == "1":

        create_account()

    elif choice == "2":

        user = login()

        if user:

            user_menu(user)

    elif choice == "3":

        save_accounts(accounts)

        print(
            "Thank you for using the system."
        )

        break

    else:

        print(
            "Invalid option."
        )
