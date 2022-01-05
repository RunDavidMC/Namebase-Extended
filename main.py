import os
from colorama import init, Fore, Back, Style
import time
import csv

import login
import bid
import listing
import generator
import status
import userinfo
import transfer

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

def menu():
  cClear()

  options = [
  "Bid on names",
  "List names for sale",
  "Generate names",
  "Get statuses on names",
  "Get user info",
  "Transfer names",]

  optOn = -1

  menuText = pName + "\n"

  num = 1

  for x in options:
    if optOn >= (len(colors) - 1):
      optOn = 0
    else:
      optOn += 1
    menuText += colors[optOn] +  "[" + str(num) + "] " + x + "\n"
    num += 1

  menuText += pName

  print(menuText)

  choice = input(Style.BRIGHT + "\nChoose an option: ")

  handler(choice)

def handler(choice):
  if choice == "1":
    bid.main(cookie)
  elif choice == "2":
    listing.main(cookie)
  elif choice == "3":
    generator.main()
  elif choice == "4":
    status.main(cookie)
  elif choice == "5":
    userinfo.main(cookie)
  elif choice == "6":
    transfer.main(cookie)
  else:
    cClear()
    print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
    time.sleep(2)
  
  menu()

cookie = login.menu()

menu()
