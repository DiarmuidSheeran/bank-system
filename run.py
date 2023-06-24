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
        go_back_key()

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
    
    def current_account_balance(self):
        """
        Function to display when promted all of the differnet accounts within the bank system.
        It shows the user the different values within different sections of their accounts.
        It gives the user information on the percentage of interest they are earning on there savings
        and what prices they had bought there investments at.
        """
        savings_projection = float(self.savings) + float(self.savings)*0.025
        print("<------------Current Account Balance Info-------------->")
        print(f"\nYour Current Account Balance is: €{self.balance}")
        print("")
        print("\n<-----------Savings Account Balance Info------------->")
        if self.savings != 0:
            print(f"\nYour Current Savings Account Balance is: €{self.savings} at a 0.025% APY")
            print(f"In one year you are expected to make €{int(self.savings)*0.025} in interest")
            print(f"Withc your current balance, your Savings account balance is projected to be at €{savings_projection} in one years time.")
        else:
            print(f"\nYour Savings Account balance is €{self.savings}")
        print("")
        print("\n<-------------Stock Balances------------>")
        print(f"\nYour Current Stock Portfolio Balance is: €{self.stocks}.\n")
        if self.google != 0:
            print(f"You have 1 share of google bought at the price of €{self.google}")
        if self.google != 0:
            print(f"You have 1 share of Apple bought at the price of €{self.apple}")
        if self.google != 0:
            print(f"You have 1 share of Meta bought at the price of €{self.meta}")
        print("")
        print("\n<-------------Cryptocurrency Balances------------->")
        print(f"\nYour Current Crypto Portfolio Balance is: €{self.crypto}.\n")
        if self.bitcoin != 0:
            print(f"You have 1 Bitcoin bought at the price of €{self.bitcoin}")
        if self.xrp != 0:
            print(f"You have 1 xrp bought at the price of €{self.xrp}")
        go_back_key()

    def deposit_to_current_account(self):
        """
        Allows the user to deposit more money to their bank balance.
        The User is prompted to enter the amount and is given their updated
        total balance
        """
        clear()
        while True:
            deposit = input("\nHow much would you like to deposit to you current account?\n")
            if char_check.search(deposit) is None and special_character_check.search(deposit) is None:
                self.balance = self.balance + float(deposit)
                clear()
                print(f"You have succesfully deposited €{deposit} to your current account.")
                print(f"Your new current account balance is €{self.balance}")
                go_back_key()
            else:
                print("\nNo special characters or letters are allowed.")
                print("Please enter a valid amount to deposit.\n")
                continue
    
    def withdraw_from_current_account(self):
        """
        Gives the user a choice to withdraw money from there account.
        A security features prompts the user to enter their account number to be able to withdraw
        money from their account.
        The amount entered is subctracted from the users balance
        """
        clear()
        while True:
            self.account_num = str(self.account_num)
            print("<-----ACCOUNT SECURITY----->")
            pin_match = input("Please enter your account number:\n")
            if pin_match == self.account_num:
                clear()
                while True:
                    withdraw = input("\nHow much would you like to withdraw from your current account?\n")
                    if char_check.search(withdraw) is None and special_character_check.search(withdraw) is None:
                        if self.balance - float(withdraw) < 0:
                            print("Insuficient funds available!")
                            print(f"Your current account balance is {self.balance}.\n")
                            while True:
                                choice = input("Would you like to make a withdrawl? (yes/no)\n")
                                if choice == "yes":
                                    clear()
                                    break
                                elif choice == "no":
                                    clear()
                                    main_menu()
                                else:
                                    print("Not a valid Option! Please type yes or no.\n")
                                    continue
                        else:
                            self.balance = self.balance - float(withdraw)
                            clear()
                            print(f"You have succesfully withdrawn €{withdraw} from your current account.")
                            print(f"Your new current account balance is €{self.balance}")
                            go_back_key()
                    else:
                        print("\nNo special characters or letters are allowed.")
                        print("Please enter a valid amount to withdraw.\n")
                        continue
            else:
                print("\nSecurity Risk, your account number is inncorect")
                go_back_key()

    def savings_account(self):
        """
        Creates a savings account within the users bank account to store money.
        Money is deposited from the Users current account (balance)
        The money (amount) is added to self.savings and subtracted from the self.balance
        If the value entered exceeds what is currently stored in balance an error prompt is called
        """
        clear()
        while True:
            amount = input("\nHow much would you like to deposit from your current account to your saving account?\n")
            if char_check.search(amount) is None and special_character_check.search(amount) is None:
                if self.balance - float(amount) < 0:
                    print("Insuficient funds available to transfer to savings account!")
                    print(f"Your current account balance is {self.balance}.\n")
                    while True:
                        choice = input("Would you like to make a transfer? (yes/no)\n")
                        if choice == "yes":
                            clear()
                            break
                        elif choice == "no":
                            clear()
                            main_menu()
                        else:
                            print("Not a valid Option! Please type yes or no.\n")
                            continue
                else:
                    self.balance = self.balance - float(amount)
                    self.savings += float(amount)
                    clear()
                    print(f"You have succesfully deposited €{amount} to your savings account.")
                    print(f"Your new savings account balance is €{self.savings}")
                    print(f"Your new current account balance is €{self.balance}")
                    go_back_key()
            else:
                print("\nNo special characters or letters are allowed.")
                print("Please enter a valid amount to deposit.\n")
                continue

    def buy_google(self):
        pass

    def buy_apple(self):
        pass
    
    def buy_meta(self):
        pass

    def google_sale(self):
        pass

    def apple_sale(self):
        pass

    def meta_sale(self):
        pass

    def stock_sale(self):
        pass

    def buy_bitcoin(self):
        pass

    def buy_xrp(self):
        pass

    def bitcoin_sale(self):
        pass

    def xrp_sale(self):
        pass

    def crypto_sale(self):
        pass

def go_back_key():
    """
    Generic function that prompts user to enter a key to be returned to main menu
    """
    while True:
        back_key = input("\nPress b to return to main menu:\n")
        if back_key == 'b':
            clear()
            break
        else: 
            print("Not a valid option!")
            continue
    main_menu()

def crypto_buy_menu():
    """
    A menu that gives users a choice of which cryptocurrencies they can buy 
    """
    clear()
    print("Warning! Trading in Cryptocurrencies is very high risk!")
    print("<--------------------->")
    print("      Choose Crypto    ")
    print("<--------------------->\n")
    print("1. Bitcoin")
    print("2. XRP")
    print("3. Main Menu")
    choice = input("Please choose between options 1 - 3:\n")
    while True:
        if choice == "1":
           initial_balance.buy_bitcoin()
        elif choice == "2":
            initial_balance.buy_xrp()
        elif choice == "3":
            main_menu()
        else:
            print("Not a valid Option! Choose between 1 - 3:\n")
            crypto_buy_menu

def crypto_sale_menu():
    """
    A menu that allows a user to sell their purchased cryptocurrencies
    """
    clear()
    print("<--------------------->")
    print("      Sell Crypto      ")
    print("<--------------------->\n")
    print("1. Sell Bitcoin")
    print("2. Sell XRP")
    print("3. Main Menu")
    choice = input("Please choose between options 1 - 3:\n")
    while True:
        if choice == "1":
           initial_balance.bitcoin_sale()
        elif choice == "2":
            initial_balance.xrp_sale()
        elif choice == "3":
            main_menu()
        else:
            print("Not a valid Option! Choose between 1 - 3:\n")
            crypto_sale_menu  

def stock_buy_menu():
    """
    A menu that gives the user an option 3 stocks to purchase"
    """
    clear()
    print("Warning! Trading in stocks can be high risk but can come with high rewards!")
    print("<--------------------->")
    print("      Choose Stock     ")
    print("<--------------------->\n")
    print("1. Google (GOOGL)")
    print("2. Apple (AAPL)")
    print("3. Meta (META)")
    print("4. Main Menu")
    choice = input("Please choose between options 1 - 4:\n")
    while True:
        if choice == "1":
           initial_balance.buy_google()
        elif choice == "2":
            initial_balance.buy_apple()
        elif choice == "3":
            initial_balance.buy_meta()
        elif choice == "4":
            main_menu()
        else:
            print("Not a valid Option! Choose between 1 - 4:\n")
            stock_buy_menu 

def stock_sales_menu():
    """
    A menu that allows a user to choose which stock they would like to sell.
    """
    clear()
    print("<------------------------------->")
    print("      Stocks Sales Menu      ")
    print("<------------------------------->\n")
    print("1. Sell Google Stock")
    print("2. Sell Apple Stock")
    print("3. Sell Meta Stcok")
    print("4. Main Menu")
    choice = input("Please choose between options 1 - 4:\n")

    while True:
        if choice == "1":
            initial_balance.google_sale()
        elif choice == "2":
            initial_balance.apple_sale()
        elif choice == "3":
            initial_balance.meta_sale()
        elif choice == "4":
            main_menu()
        else:
            print("Not a valid Option! Choose between 1 - 4:\n")
            stock_sales_menu() 

def investment_sales_menu():
    """
    Allows a user to choose which investments the would like to sell
    """
    clear()
    print("<------------------------------->")
    print("      Investment Sales Menu      ")
    print("<------------------------------->\n")
    print("1. Sell Stocks")
    print("2. Sell Cryptocurrencies")
    print("3. Main Menu")
    choice = input("Please choose between options 1 - 3:\n")

    while True:
        if choice == "1":
            initial_balance.stock_sale()
        elif choice == "2":
            initial_balance.crypto_sale()
        elif choice == "3":
            main_menu()
        else:
            print("Not a valid Option! Choose between 1 - 3:\n")
            investment_sales_menu()     

def investment_menu():
    """
    Menu that allows a user to choose which investment they want to invest in
    """
    clear()
    print("<----------------------->")
    print("      Investment Menu    ")
    print("<----------------------->\n")
    print("1. Invest in Stocks")
    print("2. Invest in Cryptocurrencies")
    print("3. Main Menu")
    choice = input("Please choose between options 1 - 3:\n")

    while True:
        if choice == "1":
            stock_buy_menu()
        elif choice == "2":
            crypto_buy_menu()
        elif choice == "3":
            main_menu()
        else:
            print("Not a valid Option! Choose between 1 - 3:\n")
            investment_menu()

def main_menu():
    """
    Systems main default menu designed for navigation around the banking application
    """
    clear()
    print("<------------------------------->")
    print(" Welcome to Sheeran's Credit Union ")
    print("<------------------------------->\n")               
    print("<------------------------------->")
    print("            Main Menu            ")
    print("<------------------------------->\n")
    print("1. Check Balance")
    print("2. Deposit to Current Account")
    print("3. Withdraw Money")
    print("4. Move to Savings")
    print("5. Investment Menu")
    print("6. Investment Sales")
    print("7. Check Account Information")
    print("8. Log out")
    choice = input("Please choose between options 1 - 8:\n")

    while True:
        if choice == "1":
            clear()
            initial_balance.current_account_balance()
        elif choice == "2":
            initial_balance.deposit_to_current_account()
        elif choice == "3":
            initial_balance.withdraw_from_current_account()
        elif choice == "4":
            initial_balance.savings_account()
        elif choice == "5":
            investment_menu()
        elif choice == "6":
            investment_sales_menu()
        elif choice == "7":
            entered_info.user_info()
        elif choice == "8":
            print("Thank you for stopping by we hape to see you again soon!")
            quit()
        else:
            print("Not a valid Option! Choose between 1 - 8:\n")
            main_menu() 

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