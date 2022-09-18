import math
from rich.console import Console
from rich.table import Table
from rich.print import Print as rprint



console = Console()
loaners = {}
bankbal = 0

def makegui():
  loanlist = Table(title="Loaner list")
  
  loanlist.add_column("Name", style="cyan", no_wrap=True)
  loanlist.add_column("Amount", style="magenta")
  
def updategui():
  for name in loaners.keys():
      loanlist.add_row(name, loaners[name])


def addloaner(name, amount):
  if name in loaners == true:
    error = "User already has a loan!"
    return error
  else:
    loaners[name] = amount
    newmoney = bankbal-loaners[name]
    money = newmoney
    success = "Success"
    return success
  
def removeloaner(name):
  if name not in loaners == true:
    error = "User has not taken a loan yet!"
    return error
  else:
    newmoney = bankbal+loaners[name]
    money = newmoney
    del loaners[name]
    success = "Success"
    return success
  


def main():






  
while True: 
  main()
