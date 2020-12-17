import hashlib
import os

def AddUser(passeduser, passedpass):
  f = open("users.txt", "a")
  hash = hashlib.sha512()
  hash.update((passedpass).encode('utf-8'))
  password_hash = hash.hexdigest()
  f.write(passeduser + ":" + password_hash + "\n")
  f.close()
def CheckUser(passeduser, passedpass):
  password_salt = os.urandom(32).hex()
  f = open("users.txt", "r")
  hash = hashlib.sha512()
  hash.update((passedpass).encode('utf-8'))
  password_hash = hash.hexdigest()
  for line in f.readlines():
    if line == passeduser + ":" + password_hash + "\n":
      return True
      break
    else:
      continue
  f.close()
def AccountCreation():
  username = input("\n\nWhat is your username?\n\n\n>>>")
  password = input("\n\nWhat is your password?\n\n\n>>>")
  if CheckUser(username, password) == True:
    print("\n\nAccount Exists\n\n")
  else:
    AddUser(username, password)
    print("\n\n")
def DeleteAccount(deletedname):
  f = open("users.txt", "r+")
  
  f.close()
def LogOn():
  username = input("\n\nWhat is your username?\n\n>>>")
  password = input("\n\nWhat is your password?\n\n>>>")
  if CheckUser(username, password) == True:
    print("\n\nLogging On As " + username + "\n\n")
    Environment(username)
  else:
    print("\n\nAccount Doesn't Exist or Password is Incorrect\n\n")

def Environment(name):
  loaded = True
  while loaded:
    print("******************************\n*                            *")
    print("*  Enter 1 to load apps      *")
    print("*  Enter 2 to delete account *")
    print("*  Enter 3 to log-out        *")
    print("*                            *")
    print("*                            *\n******************************")
    userchoice = input("\n\n>>>")
    print("\n\n")
    userint = int(userchoice)
    if userint == 1:
      print("Nothing")
    elif userint == 2:
      DeleteAccount(name)
      print("Account Deleted\n\n")
      loaded = False
    elif userint == 3:
      loaded = False
    else:
      print("Error")
def main():

  running = True
  while running:
    print("******************************\n*                            *")
    print("*  Enter 1 to create account *")
    print("*  Enter 2 to log on         *")
    print("*  Enter 3 to quit           *")
    print("*                            *\n******************************")
    print("\n\n")
    menu = input()
    menucheck = int(menu)
    if menucheck == 1:
      AccountCreation()
    elif menucheck == 2:
      LogOn()
    elif menucheck == 3:
      running = False
    else:
      print("Error")

if __name__ == "__main__":
  main()