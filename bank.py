import random #import random
import json #import json


def main_menu ():   #main menu displaying
  print("1. Create account")  #heading
  print("2. Login") #login page
  print("3. Exit") #exiting the program 
  choice = input("How can we help you today please? (1-3)  ")
  return choice
def main ():
  while True :
    choice = main_menu()
    if choice == "1":
      create_account()
    elif choice == "2":
      login()
    elif choice == "3":
      break
    else:
      print("Enter a valid choice please")
  
accounts = {} # an empty accounts dictionary for keeping accounts details
def load_accounts (): # load accounts function from json
  global accounts
  try:
    with open("accounts.json", "r") as file:
      content = file.read().strip()
      if content:
        accounts = json.loads(content)
        print("Accounts loaded:", accounts)
      else:
        accounts = {}
  except FileNotFoundError:
    accounts = {}
  except json.JSONDecodeError:
    print("Error: accounts.json contains invalid JSON.Initializing empty accounts dictionary.")
    accounts = {}    
    
def save_accounts (): # save user details to json file
  print("Saving accounts:", accounts)
  with open("accounts.json", "w") as file:
    json.dump(accounts, file, indent=4)
    
def generate_account_number ():  #generate account number func. 
  while True:
    account_number = str(random.randint(10000, 99999)) #generate random numbers with 5 digits 
    if account_number not in [account['account_number'] for account in accounts.values()]:  # check whether generated account number exists
      return account_number
    
def create_account ():    # Creating an account page
  print("Create Your Bank Account")     #heading    
  name = input("Enter your name: ")
  username = input("Create a username: ")
  password = input("Enter password: ")
  account_number = generate_account_number()
  initial_balance = 0
  
  accounts[username] = {
  "name": name, 
  "password": password, 
  "account_number": account_number, 
  "balance": initial_balance, 
  "transactions": []
  }
  
  save_accounts()     #call the function to save accounts
  print(f"{name} Your account has been created successfully. Your account number is {account_number}. Thank you. ")

def login ():
  print("Login to your Account")
  while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in accounts and accounts[username]['password'] == password:
      print(f"Welcome, {accounts[username]['name']} login successfull!")
      account_menu(username)
      break
    else:
      print("Invalid username or password.")
      retry = input("Do you want to retry again? (Yes/No) ").strip().lower()
      if retry != "Yes":
        break

def account_menu(username):
  while True:
    print("1. View Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer Money")
    print("5. View Transaction History")
    print("6. Logout")
    choice = input("What would you like to do today? ")
    
    if choice == "1":
      view_balance(username)
    elif choice =="2":
      deposit(username)
    elif choice =="3":
      withdraw(username)
    elif choice =="4":
      transfer_money(username)
    elif choice =="5":
      transaction_history(username)
    elif choice =="6":
      break
    else:
      print("Enter a valid choice please")
    
def view_balance(username):
  print(f"Your current account balance is: ${accounts[username]['balance']:.2f} ")

def deposit(username):
  amount = float(input("Enter amount to deposit: $")) 
  if amount > 0:
    accounts[username]['balance'] += amount
    accounts[username]['transactions'].append(f"Deposited ${amount:.2f} ")
    save_accounts()
    print(f"{accounts[username]['name']}, you have made a deposit of ${amount:.2f} to your account. Your new balance is {accounts[username]['balance']:.2f} ")
  else:
    print("That's not a valid amount")

def withdraw(username):
  amount = float(input("Enter amount to withdraw: $"))
  if 0 < amount <= accounts[username]['balance']:
    accounts[username]['balance'] -= amount
    accounts[username]['transactions'].append(f"Withdrawal of ${amount:.2f} ") 
    save_accounts()
    print(f"{accounts[username]['name']}, you have made a withdrawal of ${amount:.2f} from your account. Your new balance is {accounts[username]['balance']:.2f} ")
  elif amount < 0:
    print("Enter a valid amount please. ")
  else:
    print(f"Insufficient funds in your account. Balance is ${accounts[username]['balance']}")
def transfer_money(username):
  print("Send Money")
  recipient_username = input("Enter recipient username: ")
  if recipient_username not in accounts:
    print("Recipient username does not exist")
    return
  amount = float(input("Enter amount to send: $"))
  if 0 < amount <= accounts[username]['balance']:
    accounts[username]['balance'] -= amount
    accounts[recipient_username]['balance'] += amount
    
    #Log the transactions
    accounts[username]['transactions'].append(f"Transferred ${amount:.2f} to {recipient_username} ")
    accounts[recipient_username]['transactions'].append(f"Received ${amount:.2f} from {username} ")
    save_accounts()
    print(f"Your sent ${amount:.2f} to {recipient_username} ")
  else:
    print("Enter a valid amount")
    
def transaction_history(username):
  print("Transaction History")
  print("_*_*_*_*_*_*_*-*_*-*-*")
  if accounts[username]['transactions']:
    for transaction in accounts[username]['transactions']:
      print(transaction)
      
  else:
    print("No transactions found")
    
load_accounts()     #load accounts at the start of the program

if __name__ == "__main__":
  main()