from account import BankAccount

FILE_NAME = "data.txt"

def save_accounts(accounts):

    with open(FILE_NAME, "w") as file:

        for username, account in accounts.items():

            file.write(
                f"{username},{account.password},{account.balance}\n"
            )

def load_accounts():

    accounts = {}

    try:

        with open(FILE_NAME, "r") as file:

            for line in file:

                username, password, balance = (
                    line.strip().split(",")
                )

                accounts[username] = (
                    BankAccount(
                        username,
                        password,
                        balance
                    )
                )

    except FileNotFoundError:
        pass

    return accounts
