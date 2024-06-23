""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from bank import BankManager
from account import Account
Bank = BankManager()
Bank.add_account("Jimmy", 123, 4000)
Bank.display_account(123, "Jimmy", 4000)