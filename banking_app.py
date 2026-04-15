import sqlite3

DB_NAME = 'banking_app.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,  
            balance REAL NOT NULL)
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO accounts (name, balance) VALUES
        ('Alice', 1000.0),
        ('Bob', 500.0),
        ('Charlie', 750.0)
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial deposit: "))

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, balance)
    )

    connection.commit()
    connection.close()
    print("Account created successfully!")

def menu():
    print("\n=== BANKING APP ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Exit")
    

initialize_database()
