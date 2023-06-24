import random
import re
import os

# Checks if entered values contain specific charecters 
special_character_check = re.compile('[`¬!"£$%^&*()\-_+=:;#@~<>/?.,\|"]')
email_check = re.compile('@')
char_check = re.compile('[abcdefghijklmnopqrstuvwxyz]')
num_check = re.compile('[0123456789]')

def clear():
    """
    Clears the screen when called
    """
    """ 
    check if operating system is mac and linux or windows.
    """
    if os.name == 'posix':
        _ = os.system('clear')

    else:
        # else operating system is windows
        _ = os.system('cls')

class User:
    """
    Create an object for a user to be created with different properties
    """
    def __init__(self, fname, lname, age, country, email, account_num): 
        self.fname = fname
        self.lname = lname
        self.age = age
        self.country = country
        self.email = email
        self.account_num = account_num
    
    def account_created(self):
        """
        Let the user know their account has been created succesfully
        """
        print("\n-------------------------------------------")
        print(" Your Account has been created succesfully")
        print("-------------------------------------------\n")
        print("---------------------------------------------")
        print(f" Your account number is: {self.account_num}")
        print("---------------------------------------------\n")

    def user_info(self):
        """
        Function to show entered user information when prompted
        """
        clear()
        print("User Information:\n")
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname}")
        print(f"Age: {self.age}")
        print(f"Country of Residency: {self.country}")
        print(f"Email: {self.email}")
        print(f"Account Number: {self.account_num}")

class BankAccount(User):
    """
    Create a class for Bank Account to inherit values from User class.
    This will store the balance of the different accounts within the banking system
    and modify values where neccesary.
    """
    def __init__(self, fname, lname, age, country, email, account_num, balance):
        super().__init__(fname, lname, age, country, email, account_num)
        self.balance = balance
        self.savings = 0
        self.stocks = 0
        self.apple = 0
        self.google = 0
        self.meta = 0
        self.crypto = 0
        self.bitcoin = 0
        self.xrp = 0

    def initial_deposit(self):
        """
        Adds value to the overall balance of the class which can be used
        to manipulate other values within the class
        """
        self.balance = float(self.balance)
    

# Start up menu screen
print("<------------------------------->")
print(" Welcome to Sheeran's Credit Union ")
print("<------------------------------->\n")
print("<------------------------------->")
print(" Please fill in all details and \n register a new account with us ")
print("<------------------------------->\n")

while True:
    register = input("Enter 'c' to continue with registration:\n")
    if register != 'c':
        print("Not a valid option!")
        continue
    else:
        clear()
        break

# Pormpt The user to enter there details one at a time and check if charicters entered are correct
while True:
    fname = input("Please enter your first name:\n")
    if num_check.search(fname) is None and special_character_check.search(fname) is None:
        break
    else:
        print("\nNo special characters or numbers are allowed.")
        print("Please enter a valid first name.\n")
        continue
clear()
while True:
    lname = input("Please enter your last name:\n")
    if num_check.search(lname) is None and special_character_check.search(lname) is None:
            break
    else:
        print("\nNo special characters or numbers are allowed.")
        print("Please enter a valid last name.\n")
        continue
clear()
while True:
    age = input("Please enter your age:\n")
    if char_check.search(age) is None and special_character_check.search(age) is None:
        age = int(age)
        if age < 18:
            print("You must be over 18 to have a Bank Account with us.")
            continue
        else:
            break
    else:
        print("\nNo special characters or letters are allowed.")
        print("Please enter a valid age.\n")
        continue

clear()
while True:
    country = input("Please enter what country you reside in:\n")
    if num_check.search(country) is None and special_character_check.search(country) is None:
            break
    else:
        print("\nNo special characters or numbers are allowed.")
        print("Please enter a valid Country of Residence.\n")
        continue
clear()
while True:
    email = input("Please enter your email address:\n")
    if email_check.search(email):
            break
    else:
        print("\nNot a valid email address")
        print("Please enter a valid Email.\n")
        continue
clear()

# Random 4 digit number is assigned to the user for their account number
account_num = random.randint(999, 9999)

# User entered information is passed to User class
entered_info = User(fname, lname, age, country, email, account_num)
entered_info.account_created()

# User promted to enter an intial amount to their bank balance
balance = input("Please enter an amount for your initial deposit:\n")
clear()

# Add Values to bank and pass data back to initial deposit with balance amount
bank = BankAccount(fname, lname, age, country, email, account_num, balance)
bank.initial_deposit()
main_menu()