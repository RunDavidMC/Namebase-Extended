import requests
import json
import os
from colorama import init, Fore, Back, Style
import time

init(convert=True)

colors = [
  Fore.RED,
  Fore.YELLOW,
  Fore.GREEN,
  Fore.CYAN,
  Fore.BLUE,
  Fore.MAGENTA
  ]

endpoint = "https://www.namebase.io"

pName = Fore.BLUE + "--- Namebase Extended ---" + Style.RESET_ALL

def cClear():
  os.system('cls' if os.name == 'nt' else 'clear')

def lister(names):
  cClear()
  price = input(Fore.GREEN + "Enter listing price: " + Style.RESET_ALL)

  try:
    float(price)
  except:
    cClear()
    print(Fore.RED + "Invalid listing price!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  price = float(price)

  if price < 0:
    cClear()
    print(Fore.RED + "Invalid listing price!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  cClear()
  desc = input(Fore.GREEN + "Enter listing description: " + Style.RESET_ALL)

  if type(names) != list:
    names = [names]

  if len(names) == 1:
    plr = ""
  else:
    plr = "s"

  cClear()

  confirm = input(Fore.RED + "Are you sure you want to list " + str(len(names)) + " name" + plr + " for " + str(len(names) * price) + " HNS each? [y/n] " + Style.RESET_ALL)

  if confirm.lower() != "y":
    cClear()
    print(Fore.RED + "Aborting!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  params = {"amount": str(price), "asset": "HNS","description": desc}
  headers = {"Accept": 'application/json', "Content-Type": 'application/json'}

  print(params)

  for x in names:
    cClear()

    def req():

      r = requests.post(endpoint + "/api/v0/marketplace/" + x + "/list", params=params, data=json.dumps(params), headers=headers, cookies={"namebase-main": cookies}).json()

      try:
        if r['success']:
          print(Fore.GREEN + "Listing for " + x + " was successful!" + Style.RESET_ALL)
        else:
          print(Fore.RED + "An unknown error occured... Trying again.\n" + r + Style.RESET_ALL)
          time.sleep(5)
          req()
      except:
        try:
          if r['code'] == "REQUEST_UNAUTHENCIATED":
            print(Fore.RED + "Could not authenticate! Make sure your cookie is correct." + Style.RESET_ALL)
            time.sleep(5)
            return
          elif r['code'] == "REQUEST_NOT_DOMAIN_OWNER":
            print(Fore.RED + "You do not own " + x + "!" + Style.RESET_ALL)
            time.sleep(2)
          else:
            print(Fore.RED + "An unknown error occured... Trying again.\n" + r['code'] + Style.RESET_ALL)
            time.sleep(5)
            req()
        except:
          try:
            print(Fore.RED + "An unknown error occured... Trying again.\n" + r + Style.RESET_ALL)
            time.sleep(5)
            req()
          except:
            print(Fore.RED + "An unknown error occured and could not be identified... Trying again." + Style.RESET_ALL)
            time.sleep(5)
            req()

    req()

  time.sleep(20)

def menu():
  cClear()

  options = [
  "List one name",
  "List multiple names",
  "Return to main menu"
  ]

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

def singleName():
  cClear()
  name = input(Fore.GREEN + "Enter a name to list: " + Style.RESET_ALL)

  lister(name)

def multiName():
  cClear()
  file = input(Fore.GREEN + "Enter a file to import: " + Style.RESET_ALL)

  names = []

  try:
    for x in open(file, "r"):
      names.append(x.strip("\n/"))
  except FileNotFoundError:
    cClear()
    print(Fore.RED + "File not found!" + Style.RESET_ALL)
    time.sleep(2)
    multiName()

  lister(names)

def handler(choice):
  if choice == "1":
    singleName()
  elif choice == "2":
    multiName()
  elif choice == "3":
    return
  else:
    cClear()
    print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
    time.sleep(2)
  menu()

def main(cookie):
  cClear()
  
  global cookies
  cookies = cookie

  menu()
  
