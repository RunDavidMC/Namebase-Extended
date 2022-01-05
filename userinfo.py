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

def main(cookies):
  cClear()

  confirm = input(Fore.GREEN + "This command returns very sensitive data, only continue if you are not in a public area. (y/n): " + Style.RESET_ALL).lower()

  if confirm.lower() == "y":
    pass
  else: 
    print(Fore.RED + "Aborting..." + Style.RESET_ALL)
    return

  cClear()

  r = requests.get(endpoint + "/api/user", cookies={"namebase-main": cookies}).json()

  print(Fore.CYAN + "Email: " + Fore.WHITE + Style.BRIGHT + str(r['email']))
  print(Fore.CYAN + "UUID: " + Fore.WHITE + Style.BRIGHT + str(r['segmentUuid']))
  print(Fore.CYAN + "HNS Balance: " + Fore.WHITE + Style.BRIGHT + str(float(r['hns_balance']) / 1000000) + " HNS")
  if r['verificationStatus'].lower() == "verified":
    print(Fore.CYAN + "Verified: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Verified: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canLinkBank'] == True:
    print(Fore.CYAN + "Can Link Bank: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Link Bank: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canDepositHns'] == True:
    print(Fore.CYAN + "Can Deposit HNS: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Deposit HNS: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canDepositBtc'] == True:
    print(Fore.CYAN + "Can Deposit BTC: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Deposit BTC: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canDepositUsd'] == True:
    print(Fore.CYAN + "Can Deposit USD: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Deposit USD: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canWithdrawHns'] == True:
    print(Fore.CYAN + "Can Withdraw HNS: " + Fore.GREEN + Style.BRIGHT + "TRUE")  
  else:
    print(Fore.CYAN + "Can Withdraw HNS: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canWithdrawBtc'] == True:
    print(Fore.CYAN + "Can Withdraw BTC: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Withdraw BTC: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canWithdrawUsd'] == True:
    print(Fore.CYAN + "Can Withdraw USD: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Withdraw USD: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canUseProExchange'] == True:
    print(Fore.CYAN + "Can Use Pro Exchange: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Use Pro Exchange: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canUseConsumerHnsBtc'] == True:
    print(Fore.CYAN + "Can Exchange HNS/BTC: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Exchange HNS/BTC: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['canUseConsumerBtcHns'] == True:
    print(Fore.CYAN + "Can Exchange BTC/HNS: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Can Exchange BTC/HNS: " + Fore.RED + Style.BRIGHT + "FALSE")
  if r['isNewYork'] == True:
    print(Fore.CYAN + "Is New York: " + Fore.GREEN + Style.BRIGHT + "TRUE")
  else:
    print(Fore.CYAN + "Is New York: " + Fore.RED + Style.BRIGHT + "FALSE")
  print(Fore.CYAN + "Full Name: " + Style.BRIGHT + str(r['fullName']))
  print(Fore.CYAN + "Referral Code: " + Style.BRIGHT + str(r['referralCode']))


  cont = input(Fore.GREEN + "Press enter to continue. " + Style.RESET_ALL).lower()