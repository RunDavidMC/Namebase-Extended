import os
from colorama import init, Fore, Back, Style
import time
import requests

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

version = "v0.0.5a"

pName = Fore.BLUE + "--- Namebase Extended ---" + Style.RESET_ALL

def cClear():
  os.system('cls' if os.name == 'nt' else 'clear')

def updater():
  cClear()

  try:
    r = requests.get("https://api.github.com/repos/RunDavidMC/Namebase-Extended/releases/latest").json()
  except:
    print(Fore.RED + "Update check failed!" + Style.RESET_ALL)
    time.sleep(2)
    return
  try:
    if r['tag_name'].lower() != version.lower() and str(r['prerelease']).lower() == "false" and str(r['draft']).lower() == "false":
      print(Fore.GREEN + "An update is availible! Current version: " + version + ", updated version: " + r['tag_name'] + ".\nDownload it at " + Fore.CYAN + "https://github.com/RunDavidMC/Namebase-Extended/releases/latest\n" + Style.RESET_ALL)
      conf = input(Fore.GREEN + "Press enter to continue ")
  except:
    print(Fore.RED + "Update check failed!" + Style.RESET_ALL)
    time.sleep(2)
    return


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

updater()

cookie = login.menu()

menu()
