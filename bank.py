""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account
class BankManager:
    def __init__(self):
        self.accounts = []
        
    def account_exists(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
            return False
        
    def add_acount(self, account_holder, account_number, balance):
        account = self.account_exists(account_number)
        if account is not False:
            print("Account already exists.")
        else:
            new_account = Account(account_holder, account_number, balance)
            self.accounts.append(new_account)
            print(f"Account added\nNew account holder: {account_holder}\nNew account number: {account_number}")
            return True
                
    def remove_account(self, account_number, account_holder):
        account = self.account_exists(account_number)
        if account is not False:
            self.accounts.remove(account)
            print(f"Account removed\nAccount holder: {account_holder}\nAccount number: {account_number}")
            return True
        else:
            print("Account does not exist.")
            return False
            
    def deposit(self, account_number, deposit_amount):
        account = self.account_exists(account_number)
        if account is not False:
            account.deposit(deposit_amount)
            print(f"Deposited ${deposit_amount} into account {account_number}.")
            return True
        else:
            print("Account does not exist.")
            return False
            
    def withdraw(self, account_number, withdraw_amount):
        account = self.account_exists(account_number)
        if account is not False:
            account.withdraw(withdraw_amount)
            print(f"Withdrew ${withdraw_amount} from account {account_number}.")
            return True
        else:
            print("Account does not exist.")
            return False
            
    def transfer(self, account_number):
        account = self.account_exists(account_number)
        if account is not False:
            account.withdraw(withdraw_amount)            