import sqlite3

DB_NAME = "banking_app.db"


def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            balance REAL
        )
    ''')

    conn.commit()
    conn.close()


def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter deposit: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))

    conn.commit()
    conn.close()
    print("Account created!")


def deposit():
    acc_id = int(input("Enter account ID: "))
    amount = float(input("Enter amount: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, acc_id))

    conn.commit()
    conn.close()
    print("Deposit done!")


def withdraw():
    acc_id = int(input("Enter account ID: "))
    amount = float(input("Enter amount: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (acc_id,))
    result = cursor.fetchone()

    if result is None:
        print("Account not found.")
    elif result[0] < amount:
        print("Not enough balance.")
    else:
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, acc_id)
        )
        conn.commit()
        print("Withdraw done!")

    conn.close()


def check_balance():
    acc_id = int(input("Enter account ID: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, balance FROM accounts WHERE id = ?", (acc_id,))
    result = cursor.fetchone()

    if result:
        print("Name:", result[0])
        print("Balance:", result[1])
    else:
        print("Account not found.")

    conn.close()


def list_accounts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accounts")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def menu():
    print("\n--- Banking App ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Exit")


initialize_database()

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        list_accounts()
    elif choice == "6":
        break
    else:
        print("Error: Invalid choice.")