import os
import json

path = 'users'
if not os.path.exists(path):
  os.makedirs(path)

def signup():
  print("Enter your information to sign up")
  user = input("Username: ")
  user = user.lower()

  if os.path.isfile(os.path.join(path, user + ".json")) == True:
    print("Sorry, that name is taken")
    login()

  password = input("Password: ")
  password2 = input("Enter Password Again: ")

  if password != password2:
    print("Those do not match, try again")
    signup()

  data = {}
  data["username"] = user
  data["password"] = password
  data["balance"] = 0
  data["powers"] = "The Torch of Bryson!"

  with open(os.path.join(path, user + ".json"), "w") as outfile:
    json.dump(data, outfile)

def login():
  status = input("Do you have an account? y/n ")
  if status == "n":
    signup()

  print("Welcome to the login area!")
  user = input("Username: ")
  user = user.lower()
  password = input("Password: ")
  try:
    with open(os.path.join(path, user + ".json")) as json_file:
      data = json.load(json_file)
    if data["username"] == user and data["password"] == password:
      print("Logged in, welcome to the program!")
      with open("current.json", "w") as  outfile:
        json.dump(data, outfile)
    else:
      print("Incorrect username or password, try again")
      login()
  except FileNotFoundError:
    print("Sorry, we cant find your account")
    login()

login()