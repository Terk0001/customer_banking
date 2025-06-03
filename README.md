Customer Banking System

This project is a simple object-oriented banking system implemented in Python. It supports basic account management operations like creating accounts, depositing, withdrawing, and displaying balances. The system supports different account types, such as generic accounts and savings accounts.

🧾 Features

Create and manage bank accounts.
Display account details.
🗂 Project Structure

.
├── Account.py              # Base class for a generic bank account
├── savings_account.py     # Inherits from Account and adds savings-specific behavior
└── customer_banking.py    # Entry point; provides a CLI for user interaction
📦 Requirements

Python 3.x
No external dependencies
🚀 How to Run

Clone the repository or download the files.
Open a terminal and navigate to the directory containing the files.
Run the main program:
python customer_banking.py
📘 Code Overview

Account.py
Defines the Account class with:

Account creation
Deposit and withdrawal
Displaying account info
savings_account.py
Extends Account with:

Minimum balance enforcement
Overridden withdrawal behavior
customer_banking.py
A simple command-line interface to:

Create new accounts
Perform deposits/withdrawals
Display account details
Exit the system
🔒 Example Usage

Welcome to the Banking System!
1. Create Account
2. Display
3. Exit
