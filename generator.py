import os
from colorama import init, Fore, Back, Style
import time
import random
import string

init(convert=True)

colors = [
  Fore.RED,
  Fore.YELLOW,
  Fore.GREEN,
  Fore.CYAN,
  Fore.BLUE,
  Fore.MAGENTA
  ]

pName = Fore.BLUE + "--- Namebase Extended ---" + Style.RESET_ALL

def cClear():
  os.system('cls' if os.name == 'nt' else 'clear')

def gener():
  cClear()
  prefix = input(Fore.GREEN + "Enter prefix: " + Style.RESET_ALL)
  cClear()
  suffix = input(Fore.GREEN + "Enter suffix: " + Style.RESET_ALL)
  cClear()
  length = input(Fore.GREEN + "Enter length: " + Style.RESET_ALL)

  try:
    int(length)
  except:
    cClear()
    print(Fore.RED + "Invalid length!" + Style.RESET_ALL)
    time.sleep(2)
    gener()

  length = int(length)

  cClear()

  pck = input(Fore.GREEN + "Use [L]etters, [N]umbers, or [B]oth: " + Style.RESET_ALL).lower()
  while pck != "l" and pck != "n" and pck != "b":
    cClear()
    print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
    pck = input(Fore.GREEN + "Use [L]etters, [N]umbers, or [B]oth: " + Style.RESET_ALL).lower()

  cClear()

  filename = input(Fore.GREEN + "Enter file to write to: " + Style.RESET_ALL)
  cClear()
  amount = input(Fore.GREEN + "Enter amount of names to generate: " + Style.RESET_ALL)

  try:
    int(amount)
  except:
    cClear()
    print(Fore.RED + "Invalid amount!" + Style.RESET_ALL)
    time.sleep(2)
    gener()

  amount = int(amount)

  try:
    w = open(filename, 'a')
  except:
    w = open(filename, "x")
    w.close()
    w = open(filename, 'a')

  if pck == "l":
    gen = string.ascii_lowercase
  elif pck == "n":
    gen = string.digits
  else:
    gen = string.ascii_lowercase + string.digits

  nm = 0

  for x in range(amount):    
    tempName = random.sample(gen,length)
    tempName = ''.join(tempName)
    
    name = prefix + tempName + suffix

    if nm >= (len(colors) - 1):
      nm = 0
    else:
      nm += 1
    print(colors[nm] + name + Style.RESET_ALL)
    nm += 1

    w.write(name + "\n") 

  cClear()

  print(Fore.GREEN + "Successfully generated " + str(amount) + " names!" + Style.RESET_ALL)


def main():
  cClear()
  gener()
  