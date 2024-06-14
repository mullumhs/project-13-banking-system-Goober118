""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account():
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance
        
    def get_account_number(self):
        return f"Account number: {self._account_number}."
    
    def get_account_holder(self):
        return f"Account holder: {self._account_holder}."
    
    def get_balance(self):
        return f"Account balance: ${self._balance:.2f}"
    
    def set_account_number(self, account_number):
        if isinstance(account_number, int):
            self._account_number = account_number
        else:
            raise ValueError("Account number must be a number.")
    
    def set_account_holder(self, account_holder):
        for account_holder in Account:
            if isinstance(account_holder, str):
                self._account_holder = account_holder
            else:
                raise ValueError("Account holder must be a word.")
            
    def deposit(self, deposit_amount):
        self._balance + deposit_amount
        return self.get_balance()
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount < self._balance:
            self._balance - withdraw_amount
        else:  
            raise ValueError("You do not have sufficient funds.")