"""
  A bank account class. This class attempts to model a real bank account, with methods for withdrawing and depositing money. It also simulates getting bank statements.
"""

from dataclasses import dataclass
from enum import Enum

class TransactionType(str, Enum):
  DEPOSIT = "deposit"
  WITHDRAWAL = "withdrawal"

@dataclass
class Transaction:
  type: TransactionType
  amount: float
  description: str

class BankAccount():
  def __init__(self, first_name:str, last_name:str, balance:float =0):
    self.first_name =  first_name
    self.last_name = last_name
    self.balance = balance
    self.transactions: list[Transaction] = []

  def deposit(self, amount:float, description: str = "deposit"):
    if amount > 0:
      self.balance += amount
      print(f"You have successfully deposited {amount}$. Your balance is now {self.balance}$.")
      tx = Transaction(TransactionType.DEPOSIT, amount, description)
      self.transactions.append(tx)
    else:
      #print("You must deposit an amount greater than 0")
      raise ValueError("You must deposit an amount greater than 0")
      
  def withdraw(self, amount:float, description: str = "withdrawal"):
    new_balance = self.balance - amount
    if new_balance > 0:
      self.balance = new_balance
      print(f"You have successfully withdrawn {amount}$. Your balance is now {self.balance}$.")
      tx = Transaction(TransactionType.WITHDRAWAL, amount, description)
      self.transactions.append(tx)
    else:
      # print("Insufficient funds...")
      raise ValueError("Insufficient funds")

  def get_balance(self):
    print(f"Your balance is {self.balance}$")

  def get_statement(self):
    for tx in self.transactions:
      print(f"{tx.type.value.upper():10} | {tx.amount:,.2f} | {tx.description}")

my_bank_account = BankAccount("Ekomobong", "Lawrence")
my_bank_account.deposit(500)
my_bank_account.withdraw(18.55)
my_bank_account.withdraw(18.55)
my_bank_account.deposit(58.99)
my_bank_account.deposit(35.3)
my_bank_account.withdraw(18.55)
my_bank_account.withdraw(18.55)
my_bank_account.get_statement()
