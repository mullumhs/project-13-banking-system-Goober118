""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account:
class BankManager:
    def __init__(self):
        self.accounts = []
        
    def add_acount(self, account_holder, account_number, balance):
        for existing_account in self.accounts:
            