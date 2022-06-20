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

def bidder(names):
  cClear()
  bid = input(Fore.GREEN + "Enter bid amount: " + Style.RESET_ALL)

  try:
    float(bid)
  except:
    cClear()
    print(Fore.RED + "Invalid bid amount!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  bid = float(bid)

  if bid < 0:
    cClear()
    print(Fore.RED + "Invalid bid amount!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  cClear()
  blind = input(Fore.GREEN + "Enter blind amount: " + Style.RESET_ALL)

  try:
    float(blind)
  except:
    cClear()
    print(Fore.RED + "Invalid blind amount!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  blind = float(blind)

  if blind < 0:
    cClear()
    print(Fore.RED + "Invalid blind amount!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  if bid + blind < 0.4:
    cClear()
    print(Fore.RED + "Your lockup must be at least 0.4!" + Style.RESET_ALL)
    time.sleep(2)
    menu()
    
   delay = float(input("How much delay do you want in between requests (in seconds)?"))

  if type(names) != list:
    names = [names]

  if len(names) == 1:
    plr = ""
  else:
    plr = "s"

  cClear()

  confirm = input(Fore.RED + "Are you sure you want to bid a total of " + str(len(names) * (bid + blind)) + " HNS on " + str(len(names)) + " name" + plr + "? [y/n] " + Style.RESET_ALL)

  if confirm.lower() != "y":
    cClear()
    print(Fore.RED + "Aborting!" + Style.RESET_ALL)
    time.sleep(2)
    menu()

  params = {'bidAmount': str(bid), 'blindAmount': str(blind)}
  headers = {"Accept": 'application/json', "Content-Type": 'application/json'}

  print(params)

  for x in names:
    cClear()

    def req():

      r = requests.post(endpoint + "/api/v0/auction/" + x + "/bid", params=params, data=json.dumps(params), headers=headers, cookies={"namebase-main": cookies}).json()

      try:
        if r['success']:
          print(Fore.GREEN + "Bid for " + x + " was successful!" + Style.RESET_ALL)
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
          elif r['code'] == "TOO_LATE_TO_BID":
            print(Fore.RED + "Auction for " + x + " is already over!" + Style.RESET_ALL)
            time.sleep(1)
          elif r['code'] == "REQUEST_RESERVED_DOMAIN":
            print(Fore.RED + "Domain " + x + " is reserved!" + Style.RESET_ALL)
            time.sleep(1)
          elif r['code'] == "REQUEST_BID_IS_DOMINATED":
            print(Fore.RED + "Domain " + x + " is dominated!" + Style.RESET_ALL)
            time.sleep(1)
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
        
        time.sleep(delay)

    req()

  time.sleep(20)

def menu():
  cClear()

  options = [
  "Bid on one name",
  "Bid on multiple names",
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
  name = input(Fore.GREEN + "Enter a name to bid on: " + Style.RESET_ALL)

  bidder(name)

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

  bidder(names)

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
  
