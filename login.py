import os
from colorama import init, Fore, Back, Style
import time
import csv

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
  "Select account",
  "Add account"]

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

  return loginHandler(choice)

def loginHandler(choice):
  if choice == "1":
    try:
      accountsTemp = open("accounts.txt", "r")
    except:
      f = open("accounts.txt", "x")
      f.close()
      accountsTemp = open("accounts.txt", "r")

    accounts = csv.reader(accountsTemp)

    accountList = []

    for x in accounts:
      accountList.append(x)

    if len(accountList) < 1:
      cClear()
      print(Fore.RED + "No accounts found, please add one!" + Style.RESET_ALL)
      time.sleep(3)
      menu()

    cClear()

    optOn = -1

    menuText = pName + "\n"

    num = 1

    for x in accountList:
      if optOn >= (len(colors) - 1):
        optOn = 0
      else:
        optOn += 1
      menuText += colors[optOn] +  "[" + str(num) + "] " + x[0] + "\n"
      num += 1

    menuText += pName

    print(menuText)

    choice = input(Style.BRIGHT + "\nChoose an account: ")

    try:
      int(choice)
    except:
      cClear()
      print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
      time.sleep(2)
      menu()

    if int(choice) <= len(accountList):
      global cookie
      cookie = accountList[int(choice) - 1][1]
      return(cookie)
    else:
      cClear()
      print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
      time.sleep(2)
      menu()
  elif choice == "2":
    try:
      accountsTemp = open("accounts.txt", "r")
    except:
      f = open("accounts.txt", "x")
      f.close()
      accountsTemp = open("accounts.txt", "r")

    accounts = csv.reader(accountsTemp)

    cClear()

    name = input(Fore.GREEN + "Enter account name: ")

    if len(name) > 0:
      pass
    else:
      cClear()
      print(Fore.RED + "You must provide an account name!" + Style.RESET_ALL)
      time.sleep(2)
      menu()

    cClear()

    for x in accounts:
      if x[0].lower() == name.lower():
        cClear()
        print(Fore.RED + "Account already exists!" + Style.RESET_ALL)
        time.sleep(2)
        menu()

    accountsTemp.close()

    cookies = input(Fore.GREEN + "Cookies should be in this format: s%3A000000000ABCDEFGH\nFor more information on how to acquire them, visit https://git.io/JSXFC\nEnter Namebase cookies: ")

    if cookies.startswith("s%3A"):
      pass
    else:
      cClear()
      print(Fore.RED + "Incorrect cookie format!" + Style.RESET_ALL)
      time.sleep(2)
      menu()

    cClear()

    accountsWTemp = open("accounts.txt", "a", newline="")
    accountsW = csv.writer(accountsWTemp, quoting=csv.QUOTE_ALL, quotechar='"', delimiter=",")

    accountsW.writerow([name, cookies])

    accountsWTemp.close()

    cClear()
    print(Fore.GREEN + "Successfully created account " + name + "!" + Style.RESET_ALL)
    time.sleep(2)
    menu()


  else:
    cClear()
    print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
    time.sleep(2)