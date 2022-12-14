import math
from rich.pretty import pprint
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from rich.prompt import Prompt as prompt
import os


console = Console()
loaners = {}
bankbal = 0
terminalsize = os.get_terminal_size()
width = terminalsize.lines
linebreaker = "-"
choice = ""
loanlist = Table(title="Loaner list")
  
loanlist.add_column("Name", style="cyan", no_wrap=True)
loanlist.add_column("Amount", style="magenta")
      
      
def makegui():
  print("""\  __  __              ___            _   _           
 |  \/  |___ _ _  ___| _ ) __ _ _ _ | |_(_)_ _  __ _ 
 | |\/| / _ \ ' \/ _ \ _ \/ _` | ' \| / / | ' \/ _` |
 |_|  |_\___/_||_\___/___/\__,_|_||_|_\_\_|_||_\__, |
                                               |___/ """)
  print(linebreaker.ljust(width, linebreaker))
  print(loanlist)
  print(linebreaker.ljust(width, linebreaker))
  print("Balance: ", bankbal)
  print(linebreaker.ljust(width, linebreaker))
  print("Actions: \n 1 = Add a loaner \n 2 = Remove a loaner")
  choice = input("What do you want to do? ")

def addloaner():
  name = input("Name:")
  amount = input("Amount:")
  if name in loaners == true:
    error = "User already has a loan!"
    return error
  else:
    loaners[name] = amount
    newmoney = int(bankbal) - int(loaners[name])
    money = int(newmoney)
    success = "Success"
    return success
  
def removeloaner():
  name = input("Name:")
  if name not in loaners == true:
    error = "User has not taken a loan yet!"
    return error
  else:
    newmoney = int(bankbal) + int(loaners[name])
    money = int(newmoney)
    del loaners[name]
    success = "Success"
    return success
  
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')
        
def updategui():
  for name in loaners.keys():
      loanlist.add_row(name, loaners[name]
   clear()
   makegui()

def main():
  makegui()
  if choice == "1":
    addloaner()
    updategui()
  if choice == "2": 
    removeloaner()
    updategui()
  
while True: 
  main()
