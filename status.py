import requests
import json
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

endpoint = "https://www.namebase.io"

pName = Fore.BLUE + "--- Namebase Extended ---" + Style.RESET_ALL

def cClear():
  os.system('cls' if os.name == 'nt' else 'clear')

def menu():
  cClear()

  options = [
  "Get status on all my domains",
  "Get all ending soon domains",
  "Get marketplace domains",
  "Get status on a single domain",
  "Get status on multiple domains",
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

def myDoms():
  cClear()

  mode = input(Fore.GREEN + "[S]imple or [A]dvanced mode? " + Style.RESET_ALL).lower()

  while mode != "s" and mode != "a":
    cClear()
    print(Fore.RED + "Invalid mode!" + Style.RESET_ALL)
    mode = input(Fore.GREEN + "[S]imple or [A]dvanced mode? " + Style.RESET_ALL).lower()

  cClear()

  types = input(Fore.GREEN + "Get [O]ff sale or on [S]ale domains? " + Style.RESET_ALL).lower()

  while types != "o" and types != "s":
    cClear()
    print(Fore.RED + "Invalid type!" + Style.RESET_ALL)
    types = input(Fore.GREEN + "Get [O]ff sale, on [S]ale, or [B]oth? " + Style.RESET_ALL).lower()

  cClear()

  filename = input(Fore.GREEN + "Enter file to write to: " + Style.RESET_ALL)

  try:
    fileTemp = open(filename, "w", newline="")
  except:
    fileTemp = open(filename, "x")
    fileTemp.close()
    fileTemp = open(filename, "w", newline="")

  cClear()
  print(Fore.GREEN + "Getting domains..." + Style.RESET_ALL)

  r = requests.get(endpoint + "/api/user/domains/not-listed/0", cookies={"namebase-main": cookies}).json()

  try:
    if r['success'] == False:
      print(Fore.RED + "Error: " + r['code'] + Style.RESET_ALL)
      time.sleep(2)
      menu()
  except:
    if r['code'] == "REQUEST_UNAUTHENCIATED":
      print(Fore.RED + "Could not authenticate! Make sure your cookie is correct." + Style.RESET_ALL)
      time.sleep(5)
      return

  total = r['totalCount']

  doms = []
  offset = 0
# Not listed
  if types == "o":

    while total > 0:
      total -= 100
      r = requests.get(endpoint + f"/api/user/domains/not-listed/{str(offset)}" + "?sortKey=acquiredAt&sortDirection=desc&limit=100", cookies={"namebase-main": cookies}).json()
      [doms.append(i) for i in r['domains']]
      offset += 100
    
    if mode == "a":
      file = csv.writer(fileTemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      file.writerow(["Name", "Views", "Renewal Block", "Uses NB Servers"])
      for x in doms:
        file.writerow([x['name'], x['numberViews'], x['renewalBlock'], x['usesOurNameservers']])
    else:
      for x in doms:
        print(x['name'])
        fileTemp.write(x['name'] + "\n")
# Listed for sale
  if types == "s":
    while len(r['domains']) > 0:
      r = requests.get(endpoint + f"/api/user/domains/listed/{str(offset)}", cookies={"namebase-main": cookies}).json()
      [doms.append(i) for i in r['domains']]
      offset += 15
    if mode == "a": # Advanced
      file = csv.writer(fileTemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      file.writerow(["Name", "Price", "Renewal Block"])
      for x in doms:
        file.writerow([x['name'], float(x['amount']) / 1000000, x['renewalBlock']])
    else: # Simple
      for x in doms:
        print(x['name'])
        fileTemp.write(x['name'] + "\n")


  fileTemp.close()
  print(Fore.GREEN + "Successfully got names!" + Style.RESET_ALL)

  time.sleep(2)


def ending():
  cClear()

  mode = input(Fore.GREEN + "[S]imple or [A]dvanced mode? " + Style.RESET_ALL).lower()

  while mode != "s" and mode != "a":
    cClear()
    print(Fore.RED + "Invalid mode!" + Style.RESET_ALL)
    mode = input(Fore.GREEN + "[S]imple or [A]dvanced mode? " + Style.RESET_ALL).lower()

  cClear()

  filename = input(Fore.GREEN + "Enter file to write to: " + Style.RESET_ALL)

  try:
    fileTemp = open(filename, "w", newline="")
  except:
    fileTemp = open(filename, "x")
    fileTemp.close()
    fileTemp = open(filename, "w", newline="")

  cClear()
  print(Fore.GREEN + "Getting domains..." + Style.RESET_ALL)

  try:
    r = requests.get(endpoint + "/api/domains/ending-soon/0?limit=100").json()
  except:
    print(Fore.RED + "Could not get domains! Please try again later." + Style.RESET_ALL)
  
  doms = []
  [doms.append(i) for i in r['domains']]

  if mode == "a":
    file = csv.writer(fileTemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    file.writerow(["Name", "Bids", "Reveal Block"])
    for x in doms:
      file.writerow([x['name'], x['total_number_bids'], x['reveal_block']])
  else:
    for x in doms:
      print(x['name'])
      fileTemp.write(x['name'] + "\n")

  fileTemp.close()
  print(Fore.GREEN + "Successfully got names!" + Style.RESET_ALL)

  time.sleep(2)

def marketplace():
  cClear()

  mode = input(Fore.GREEN + "[S]imple or [A]dvanced mode? " + Style.RESET_ALL).lower()

  while mode != "s" and mode != "a":
    cClear()
    print(Fore.RED + "Invalid mode!" + Style.RESET_ALL)
    mode = input(Fore.GREEN + "[S]imple or [A]dvanced mode? " + Style.RESET_ALL).lower()

  cClear()

  filename = input(Fore.GREEN + "Enter file to write to: " + Style.RESET_ALL)

  try:
    fileTemp = open(filename, "w", newline="")
  except:
    fileTemp = open(filename, "x")
    fileTemp.close()
    fileTemp = open(filename, "w", newline="")

  cClear()
  print(Fore.GREEN + "Getting domains..." + Style.RESET_ALL)

  try:
    r = requests.get(endpoint + "/api/domains/marketplace/0").json()
  except:
    print(Fore.RED + "Could not get domains! Please try again later." + Style.RESET_ALL)
  
  doms = []

  [doms.append(i) for i in r['domains']]

  print(doms)

  if mode == "a":
    file = csv.writer(fileTemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    file.writerow(["Name", "Price", "ID"])
    for x in doms:
      file.writerow([x['name'], float(x['amount']) / 1000000, x['id']])
  else:
    for x in doms:
      print(x['name'])
      fileTemp.write(x['name'] + "\n")

  fileTemp.close()
  print(Fore.GREEN + "Successfully got names!" + Style.RESET_ALL)

  time.sleep(2)

def status(names, filename=""):
  if type(names) != list:
    names = [names]

  doms = []

  for x in names:
    r = requests.get(endpoint + "/api/domains/get/" + x).json()
    doms.append(r)

  if filename != "":
    try:
      fileTemp = open(filename, "w", newline="")
    except:
      fileTemp = open(filename, "x")
      fileTemp.close()
      fileTemp = open(filename, "w", newline="")

    file = csv.writer(fileTemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    file.writerow(["Name", "Bids", "Views", "Release Block", "Open Block", "Reveal Block", "Close Block", "Winning Bid", "Highest Lockup", "Watching", "Reserved"])

    for x in doms:
      try:
        closeAmount = float(x['closeAmount']) / 1000000
      except:
        closeAmount = x['closeAmount']
      try:
        stakeAmount = float(x['highestStakeAmount']) / 1000000
      except:
        stakeAmount = x['highestStakeAmount']
      file.writerow([x['name'], len(x['bids']), x['numberViews'], x['releaseBlock'], x['openBlock'], x['revealBlock'], x['closeBlock'], closeAmount, stakeAmount, x['numWatching'], x['reserved']])

    fileTemp.close()

  print(Fore.GREEN + "Successfully got status!" + Style.RESET_ALL)

def single():
  cClear()

  name = input(Fore.GREEN + "Enter name: " + Style.RESET_ALL)

  status(name)

def multi():
  cClear()

  filename = input(Fore.GREEN + "Enter file to read from: " + Style.RESET_ALL)

  cClear()

  doms = []

  try: 
    file = open(filename, "r")
  except:
    print(Fore.RED + "File not found!" + Style.RESET_ALL)
    return

  for x in file:
    doms.append(x.strip("\n/"))

  filename2 = input(Fore.GREEN + "Enter file to write to: " + Style.RESET_ALL)

  status(doms, filename2)

def handler(choice):
  if choice == "1":
    myDoms()
  elif choice == "2":
    ending()
  elif choice == "3":
    marketplace()
  elif choice == "4":
    single()
  elif choice == "5":
    multi()
  elif choice == "6":
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
  
