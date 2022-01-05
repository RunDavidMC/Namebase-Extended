import requests
import json
import pyotp
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

  mode = input(Fore.GREEN + "Use [T]OTP seed or [M]anually enter TOTP codes: " + Style.RESET_ALL).lower()
  while mode != "t" and mode != "m":
    cClear()
    mode = input(Fore.RED + "Invalid mode!" + Style.RESET_ALL).lower()
    mode = input(Fore.GREEN + "Use [T]OTP seed or [M]anually enter TOTP codes: " + Style.RESET_ALL).lower()

  cClear()

  address = input(Fore.GREEN + "Enter HNS Address to send to: " + Style.RESET_ALL).lower()

  if address.startswith("hs1"):
    pass
  else:
    cClear()
    print(Fore.RED + "Invalid HNS Address!" + Style.RESET_ALL)
    time.sleep(2)
    return

  cClear()

  filename = input(Fore.GREEN + "Enter file to read from: " + Style.RESET_ALL)

  cClear()
  
  try:
    file = open(filename, "r")
  except:
    file = open(filename, "x")
    file.close()
    file = open(filename, "r")

  params = {"address" : address}

  if mode == "t":
    totp = input(Fore.GREEN + "Enter TOTP seed: " + Style.RESET_ALL)
    totp = pyotp.TOTP(totp)

    for x in file:

      try:
        headers = {"Accept": "application/json", "Content-Type": "application/json", "x-totp-tokens": str(totp.now())}
      except:
        cClear()
        print(Fore.RED + "Invalid TOTP seed!" + Style.RESET_ALL)
        time.sleep(2)
        return

      r = requests.post("https://www.namebase.io/api/domains/" + x.strip("\n/") + "/transfer/", headers=headers, data=json.dumps(params), cookies={"namebase-main": cookies}).json()

      try:
        if r['success'] == True:
          print(Fore.GREEN + "Successfully transferred " + x.strip("\n/") + " to " + address + Style.RESET_ALL)
        else:
          print(r)
      except:
        try:
          if r['code'] == "MFA_BAD_VERIFICATION_CODE":
            time.sleep(2)
            r = requests.post("https://www.namebase.io/api/domains/" + x.strip("\n/") + "/transfer/", headers=headers, data=json.dumps(params), cookies={"namebase-main": cookies}).json()
            if r['code'] == "MFA_BAD_VERIFICATION_CODE":
              cClear()
              print(Fore.RED + "Invalid TOTP seed!" + Style.RESET_ALL)
              time.sleep(2)
              return
            elif r['code'] == "REQUEST_UNAUTHENCIATED":
              cClear()
              print(Fore.RED + "Unable to authenticate. Make sure your cookie is correct!" + Style.RESET_ALL)
              time.sleep(2)
              return
        except:
          pass

  else:
    code = input(Fore.GREEN + "Enter TOTP code: " + Style.RESET_ALL)

    for x in file:

      headers = {"Accept": "application/json", "Content-Type": "application/json", "x-totp-tokens": code}

      r = requests.post("https://www.namebase.io/api/domains/" + x.strip("\n/") + "/transfer/", headers=headers, data=json.dumps(params), cookies={"namebase-main": cookies}).json()

      try:
        if r['success'] == True:
          print(Fore.GREEN + "Successfully transferred " + x.strip("\n/") + " to " + address + Style.RESET_ALL)
        else:
          print(r)
      except:
        try:
          if r['code'] == "MFA_BAD_VERIFICATION_CODE":
            code = input(Fore.GREEN + "TOTP code expired, please enter a new one: " + Style.RESET_ALL)
          elif r['code'] == "REQUEST_UNAUTHENCIATED":
            cClear()
            print(Fore.RED + "Unable to authenticate. Make sure your cookie is correct!" + Style.RESET_ALL)
            time.sleep(2)
            return
        except:
          pass

