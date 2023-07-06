import random
import re
import os

# Checks if entered values contain specific charecters
special_character_check = re.compile(r'[`¬!"£$%^&*()\-_+=:;#@~<>/?.,\|"]')
email_check = re.compile("@.")
char_check = re.compile("[abcdefghijklmnopqrstuvwxyz]")
num_check = re.compile("[0123456789]")


def clear():
    """
    Clears the screen when called
    check if operating system is mac and linux or windows.
    """
    if os.name == "posix":
        _ = os.system("clear")

    else:
        # else operating system is windows
        _ = os.system("cls")


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
    This will store the balance of the different accounts within the banking
    system
    and modify values where neccesary.
    """

    def __init__(self, fname, lname, age, country, email, account_num,
                 balance):
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
        Function to display when promted all of the differnet accounts within
        the bank system.
        It shows the user the different values within different sections of
        their accounts.
        It gives the user information on the percentage of interest they are
        earning on there savings
        and what prices they had bought there investments at.
        """
        savings_projection = float(self.savings) + float(self.savings) * 0.025
        print("<------------Current Account Balance Info-------------->")
        print(f"\nYour Current Account Balance is: €{self.balance}")
        print("")
        print("\n<------------Savings Account Balance Info-------------->")
        if self.savings != 0:
            print(
                f"\nYour Current Savings Account Balance is: €{self.savings}"
                f" \nat a 0.025% APY"
            )
            print(
                f"In one year you are expected to make"
                f" \n€{int(self.savings)*0.025} in interest"
            )
            print(
                f"With your current balance, your Savings account balance is"
                f" \nprojected to be at €{savings_projection} in one years time."
            )
        else:
            print(f"\nYour Savings Account balance is €{self.savings}")
        print("")
        print("\n<--------------------Stock Balances------------------->")
        print(f"\nYour Current Stock Portfolio Balance is: €{self.stocks}.\n")
        if self.google != 0:
            print(f"You have 1 share of google bought at the price of"
                  f" €{self.google}")
        if self.apple != 0:
            print(f"You have 1 share of Apple bought at the price of"
                  f" €{self.apple}")
        if self.meta != 0:
            print(f"You have 1 share of Meta bought at the price of"
                  f" €{self.meta}")
        print("")
        print("\n<---------------Cryptocurrency Balances--------------->")
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
            try:
                deposit = input(
                    "\nHow much would you like to deposit to you current"
                    " account?\n"
                )
                if not deposit:
                    print("No Data Entered\n")
                    continue
                if (
                    char_check.search(deposit) is None
                    and special_character_check.search(deposit) is None
                ):
                    self.balance = self.balance + float(deposit)
                    clear()
                    print(
                        f"You have succesfully deposited €{deposit} to your"
                        f" current account."
                    )
                    print(f"Your new current account balance is €{self.balance}")
                    go_back_key()
                else:
                    print("\nNo special characters or letters are allowed.")
                    print("Please enter a valid amount to deposit.\n")
                    continue
            except ValueError:
                print("\nNot a valid entry\n")
                continue

    def withdraw_from_current_account(self):
        """
        Gives the user a choice to withdraw money from there account.
        A security features prompts the user to enter their account number
        to be able to withdraw
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
                    try:
                        withdraw = input(
                            "\nHow much would you like to withdraw from your"
                            " current account?\n"
                        )
                        if not withdraw:
                            print("No Data Entered\n")
                            continue
                        if (
                            char_check.search(withdraw) is None
                            and special_character_check.search(withdraw) is None
                        ):
                            if self.balance - float(withdraw) < 0:
                                print("Insuficient funds available!")
                                print(f"Your current account balance is"
                                    f" {self.balance}.\n")
                                while True:
                                    choice = input(
                                        "Would you like to make a withdrawl?"
                                        " (yes/no)\n"
                                    )
                                    if choice == "yes":
                                        clear()
                                        break
                                    elif choice == "no":
                                        clear()
                                        main_menu()
                                    else:
                                        print(
                                            "Not a valid Option! Please type"
                                            " yes or no.\n"
                                        )
                                        continue
                            else:
                                self.balance = self.balance - float(withdraw)
                                clear()
                                print(
                                    f"You have succesfully withdrawn €{withdraw}"
                                    f" from your current account."
                                )
                                print(
                                    f"Your new current account balance is"
                                    f" €{self.balance}"
                                )
                                go_back_key()
                        else:
                            print("\nNo special characters or letters"
                                " are allowed.")
                            print("Please enter a valid amount to withdraw.\n")
                            continue
                    except ValueError:
                        print("\nNot a valid entry\n")
                        continue
            else:
                print("\nSecurity Risk, your account number is inncorect")
                print("\nYou can find your account number in account info"
                      "\n section at the main menu")
                go_back_key()

    def savings_account(self):
        """
        Creates a savings account within the users bank account to store money.
        Money is deposited from the Users current account (balance)
        The money (amount) is added to self.savings and subtracted from
        the self.balance
        If the value entered exceeds what is currently stored
        in balance an error prompt is called
        """
        clear()
        while True:
            try:
                amount = input(
                    "\nHow much would you like to deposit from your current"
                    " account \nto your saving account?\n"
                )
                if not amount:
                    print("No Data Entered\n")
                    continue
                if (
                    char_check.search(amount) is None
                    and special_character_check.search(amount) is None
                ):
                    if self.balance - float(amount) < 0:
                        print("Insuficient funds available to transfer to savings"
                            " \naccount!")
                        print(f"Your current account balance is {self.balance}.\n")
                        while True:
                            choice = input(
                                "Would you like to make a transfer? (yes/no)\n"
                            ).lower()
                            if choice == "yes":
                                clear()
                                break
                            elif choice == "no":
                                clear()
                                main_menu()
                            else:
                                print("Not a valid Option! Please type yes or"
                                    " no.\n")
                                continue
                    else:
                        self.balance = self.balance - float(amount)
                        self.savings += float(amount)
                        clear()
                        print(
                            f"You have succesfully deposited €{amount} to your"
                            f" \nsavings account."
                        )
                        print(f"Your new savings account balance is"
                            f" \n€{self.savings}")
                        print(f"Your new current account balance is"
                            f" \n€{self.balance}")
                        go_back_key()
                else:
                    print("\nNo special characters or letters are allowed.")
                    print("Please enter a valid amount to deposit.\n")
                    continue
            except ValueError:
                print("\nNot a valid entry\n")
                continue

    def buy_google(self):
        """
        Gives google stock a random value between 200 and 350
        Only allows user to purchase 1 share
        Wont allow user to purchase stock at the price if their balance
        is below the value
        Updates stocks and google variables with the values added if purchased
        Balances are updated accordinaly
        """
        clear()
        google = random.randint(200, 350)
        if self.google != 0:
            print("You are only able to hold one share at a time!")
            go_back_key()
        else:
            while True:
                clear()
                print(f"Google is currently trading at: €{str(google)}"
                      f" a share.")
                choice = input(
                    "\nWould you like to purchase 1 share in Google?"
                    " (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.balance - float(google) < 0:
                        print("Insuficient funds available to buy this stock")
                        print(f"Your current account balance is"
                              f" {self.balance}.\n")
                        go_back_key()
                    else:
                        self.balance = self.balance - float(google)
                        self.stocks += float(google)
                        self.google += float(google)
                        clear()
                        print("Congratulations!\n")
                        print(
                            f"You have succesfully bought 1 share in Google"
                            f" trading at €{str(google)} a share."
                        )
                        go_back_key()
                elif choice == "no":
                    stock_buy_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def buy_apple(self):
        """
        Gives Apple stock a random value between 400 and 650
        Only allows user to purchase 1 share
        Wont allow user to purchase stock at the price if their
        balance is below the value
        Updates stocks and apple variables with the values added if purchased
        Balances are updated accordinaly
        """
        clear()
        apple = random.randint(400, 650)
        if self.apple != 0:
            print("You are only able to hold one share at a time!")
            go_back_key()
        else:
            while True:
                clear()
                print(f"Apple is currently trading at: €{str(apple)} a share.")
                choice = input(
                    "\nWould you like to purchase 1 share in Apple? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.balance - float(apple) < 0:
                        print("Insuficient funds available to buy this stock")
                        print(f"Your current account balance is"
                              f" {self.balance}.\n")
                        go_back_key()
                    else:
                        self.balance = self.balance - float(apple)
                        self.stocks += float(apple)
                        self.apple += float(apple)
                        clear()
                        print("Congratulations!\n")
                        print(
                            f"You have succesfully bought 1 share in Apple"
                            f" trading at €{str(apple)} a share."
                        )
                        go_back_key()
                elif choice == "no":
                    stock_buy_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def buy_meta(self):
        """
        Gives Meta stock a random value between 50 and 150
        Only allows user to purchase 1 share
        Wont allow user to purchase stock at the price if their
        balance is below the value
        Updates stocks and meta variables with the values added if purchased
        Balances are updated accordinaly
        """
        clear()
        meta = random.randint(50, 150)
        if self.meta != 0:
            print("You are only able to hold one share at a time!")
            go_back_key()
        else:
            while True:
                clear()
                print(f"Meta is currently trading at: €{str(meta)} a share.")
                choice = input(
                    "\nWould you like to purchase 1 share in Meta? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.balance - float(meta) < 0:
                        print("Insuficient funds available to buy this stock")
                        print(f"Your current account balance is"
                              f" {self.balance}.\n")
                        go_back_key()
                    else:
                        self.balance = self.balance - float(meta)
                        self.stocks += float(meta)
                        self.meta += float(meta)
                        clear()
                        print("Congratulations!\n")
                        print(
                            f"You have succesfully bought 1 share in Meta"
                            f" trading at €{str(meta)} a share."
                        )
                        go_back_key()
                elif choice == "no":
                    stock_buy_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def google_sale(self):
        """
        Assingns a random value to a new variable to create a new stock price
        The new stock price is compared to the origianlly purcheaed price
        A calcululation is made for whether it is a profit or a loss.
        The new variable stock price is add to the users balance.
        The User is given a summary on whether they made a profit or a loss.
        """
        clear()
        google_current_price = random.randint(200, 350)
        if self.google == 0:
            print("You have no money invested in Google!")
            go_back_key()
        else:
            while True:
                print(
                    f"Googles price is currently trading at"
                    f" €{str(google_current_price)}. You bought it"
                    f" at €{(self.google)}"
                )
                choice = input(
                    "Would you like to sell your share in Google? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.google > google_current_price:
                        loss = self.google - google_current_price
                        self.stocks -= self.google
                        self.google = 0
                        self.balance += google_current_price
                        clear()
                        print(f"You have sold your Google Stock at a loss"
                              f" of €{loss}")
                        print(
                            f"€{google_current_price} has been added to"
                            f" your current account."
                        )
                        go_back_key()
                    elif self.google < google_current_price:
                        profit = google_current_price - self.google
                        self.stocks -= self.google
                        self.google = 0
                        self.balance += google_current_price
                        clear()
                        print(
                            f"You have sold your Google Stock at a profit of"
                            f" €{profit}"
                        )
                        print(
                            f"€{google_current_price} has been added to your"
                            f" current account."
                        )
                        go_back_key()
                elif choice == "no":
                    stock_sales_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def apple_sale(self):
        """
        Assingns a random value to a new variable to create a new stock price
        The new stock price is compared to the origianlly purcheaed price
        A calcululation is made for whether it is a profit or a loss.
        The new variable stock price is add to the users balance.
        The User is given a summary on whether they made a profit or a loss.
        """
        clear()
        apple_current_price = random.randint(400, 650)
        if self.apple == 0:
            print("You have no money invested in Apple!")
            go_back_key()
        else:
            while True:
                print(
                    f"Apples price is currently trading at"
                    f" €{str(apple_current_price)}."
                    f" You bought it at €{(self.apple)}"
                )
                choice = input(
                    "Would you like to sell your share in Apple? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.apple > apple_current_price:
                        loss = self.apple - apple_current_price
                        self.stocks -= self.apple
                        self.apple = 0
                        self.balance += apple_current_price
                        clear()
                        print(f"You have sold your Apple Stock at a loss"
                              f" of €{loss}")
                        print(
                            f"€{apple_current_price} has been added to your"
                            f" current account."
                        )
                        go_back_key()
                    elif self.apple < apple_current_price:
                        profit = apple_current_price - self.apple
                        self.stocks -= self.apple
                        self.apple = 0
                        self.balance += apple_current_price
                        clear()
                        print(
                            f"You have sold your Apple Stock at a profit"
                            f" of €{profit}"
                        )
                        print(
                            f"€{apple_current_price} has been added to your"
                            f" current account."
                        )
                        go_back_key()
                elif choice == "no":
                    stock_sales_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def meta_sale(self):
        """
        Assingns a random value to a new variable to create a new stock price
        The new stock price is compared to the origianlly purcheaed price
        A calcululation is made for whether it is a profit or a loss.
        The new variable stock price is add to the users balance.
        The User is given a summary on whether they made a profit or a loss.
        """
        clear()
        meta_current_price = random.randint(50, 150)
        if self.meta == 0:
            print("You have no money invested in Meta!")
            go_back_key()
        else:
            while True:
                print(
                    f"Meta price is currently trading at"
                    f" €{str(meta_current_price)}. You bought it at"
                    f" €{(self.meta)}"
                )
                choice = input(
                    "Would you like to sell your share in Meta? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.meta > meta_current_price:
                        loss = self.meta - meta_current_price
                        self.stocks -= self.meta
                        self.meta = 0
                        self.balance += meta_current_price
                        clear()
                        print(f"You have sold your Meta Stock at a loss"
                              f" of €{loss}")
                        print(
                            f"€{meta_current_price} has been added to"
                            f" your current account."
                        )
                        go_back_key()
                    elif self.meta < meta_current_price:
                        profit = meta_current_price - self.meta
                        self.stocks -= self.meta
                        self.meta = 0
                        self.balance += meta_current_price
                        clear()
                        print(f"You have sold your Meta Stock at a profit"
                              f" of €{profit}")
                        print(
                            f"€{meta_current_price} has been added to"
                            f" your current account."
                        )
                        go_back_key()
                elif choice == "no":
                    stock_sales_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def stock_sale(self):
        """
        Denies user entry if balance of stocks is below 0
        """
        clear()
        if self.stocks == 0:
            print("You have no money invested in stocks!")
            go_back_key()
        else:
            stock_sales_menu()

    def buy_bitcoin(self):
        """
        Gives Bitcoin a random value between 10000 and 100000
        Only allows user to purchase 1 coin
        Wont allow user to purchase crypto at the price if their
        balance is below the value
        Updates crypto and bitcoin variables with the values added if purchased
        Balances are updated accordinaly
        """
        clear()
        bitcoin = random.randint(10000, 100000)
        if self.bitcoin != 0:
            print("You are only able to hold one Crypto coin at a time!")
            go_back_key()
        else:
            while True:
                clear()
                print(f"Bitcoin is currently trading at: €{str(bitcoin)}.")
                choice = input(
                    "\nWould you like to purchase 1 Bitcoin? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.balance - float(bitcoin) < 0:
                        print("Insuficient funds available to buy"
                              " this cryptocurrency")
                        print(f"Your current account balance is"
                              f" {self.balance}.\n")
                        go_back_key()
                    else:
                        self.balance = self.balance - float(bitcoin)
                        self.crypto += float(bitcoin)
                        self.bitcoin += float(bitcoin)
                        clear()
                        print("Congratulations!\n")
                        print(
                            f"You have succesfully bought 1 Bitcoin trading"
                            f" at €{str(bitcoin)}"
                        )
                        go_back_key()
                elif choice == "no":
                    crypto_buy_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def buy_xrp(self):
        """
        Gives xrp a random value between 1 and 200
        Only allows user to purchase 1 coin
        Wont allow user to purchase crypto at the price if their balance
        is below the value
        Updates crypto and xrp variables with the values added if purchased
        Balances are updated accordinaly
        """
        clear()
        xrp = random.randint(1, 200)
        if self.xrp != 0:
            print("You are only able to hold one Crypto coin at a time!")
            go_back_key()
        else:
            while True:
                clear()
                print(f"XRP is currently trading at: €{str(xrp)}.")
                choice = input("\nWould you like to purchase 1 XRP?"
                               " (yes/no)\n").lower()
                if choice == "yes":
                    if self.balance - float(xrp) < 0:
                        print("Insuficient funds available to buy this"
                              " cryptocurrency")
                        print(f"Your current account balance is"
                              f" {self.balance}.\n")
                        go_back_key()
                    else:
                        self.balance = self.balance - float(xrp)
                        self.crypto += float(xrp)
                        self.xrp += float(xrp)
                        clear()
                        print("Congratulations!\n")
                        print(
                            f"You have succesfully bought 1 XRP trading at"
                            f" €{str(xrp)}"
                        )
                        go_back_key()
                elif choice == "no":
                    crypto_buy_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def bitcoin_sale(self):
        """
        Assingns a random value to a new variable to create a new crypto price
        The new crypto price is compared to the origianlly purcheaed price
        A calcululation is made for whether it is a profit or a loss.
        The new variable crypto price is add to the users balance.
        The User is given a summary on whether they made a profit or a loss.
        """
        clear()
        bitcoin_current_price = random.randint(10000, 100000)
        if self.bitcoin == 0:
            print("You have no money invested in Bitcoin!")
            go_back_key()
        else:
            while True:
                print(
                    f"Bitcoin price is currently trading at"
                    f" €{str(bitcoin_current_price)}. You bought it at"
                    f" €{(self.bitcoin)}"
                )
                choice = input(
                    "Would you like to sell your share in Bitcoin? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.bitcoin > bitcoin_current_price:
                        loss = self.bitcoin - bitcoin_current_price
                        self.crypto -= self.bitcoin
                        self.bitcoin = 0
                        self.balance += bitcoin_current_price
                        clear()
                        print(f"You have sold your Bitcoin at a loss of"
                              f" €{loss}")
                        print(
                            f"€{bitcoin_current_price} has been added to your"
                            f" current account."
                        )
                        go_back_key()
                    elif self.bitcoin < bitcoin_current_price:
                        profit = bitcoin_current_price - self.bitcoin
                        self.crypto -= self.bitcoin
                        self.bitcoin = 0
                        self.balance += bitcoin_current_price
                        clear()
                        print(f"You have sold your Bitcoin at a profit of"
                              f" €{profit}")
                        print(
                            f"€{bitcoin_current_price} has been added to your"
                            f" current account."
                        )
                        go_back_key()
                elif choice == "no":
                    crypto_sale_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def xrp_sale(self):
        """
        Assingns a random value to a new variable to create a new crypto price
        The new crypto price is compared to the origianlly purcheaed price
        A calcululation is made for whether it is a profit or a loss.
        The new variable crypto price is add to the users balance.
        The User is given a summary on whether they made a profit or a loss.
        """
        clear()
        xrp_current_price = random.randint(1, 200)
        if self.xrp == 0:
            print("You have no money invested in XRP!")
            go_back_key()
        else:
            while True:
                print(
                    f"XRP price is currently trading at"
                    f" €{str(xrp_current_price)}. You bought it at"
                    f" €{(self.xrp)}"
                )
                choice = input(
                    "Would you like to sell your share in Bitcoin? (yes/no)\n"
                ).lower()
                if choice == "yes":
                    if self.xrp > xrp_current_price:
                        loss = self.xrp - xrp_current_price
                        self.crypto -= self.xrp
                        self.xrp = 0
                        self.balance += xrp_current_price
                        clear()
                        print(f"You have sold your XRP at a loss of €{loss}")
                        print(
                            f"€{xrp_current_price} has been added to your"
                            f" current account."
                        )
                        go_back_key()
                    elif self.xrp < xrp_current_price:
                        profit = xrp_current_price - self.xrp
                        self.crypto -= self.xrp
                        self.xrp = 0
                        self.balance += xrp_current_price
                        clear()
                        print(f"You have sold your XRP at a profit of"
                              f" €{profit}")
                        print(
                            f"€{xrp_current_price} has been added to your"
                            f" current account."
                        )
                        go_back_key()
                elif choice == "no":
                    crypto_sale_menu()
                else:
                    print("Not a valid Option! Please type yes or no.\n")
                    continue

    def crypto_sale(self):
        """
        Denies user entry if balance of crypto is below 0
        """
        clear()
        if self.crypto == 0:
            print("You have no money invested in cryptocurrencies!")
            go_back_key()
        else:
            crypto_sale_menu()

    def quiz_prize(self):
        """
        If user scores 100% in the quiz this function will add the stock to the
        users account
        or money to their current account
        """
        google = random.randint(200, 350)
        if self.google != 0:
            self.balance += float(google)
            print("\nYou already own a share in Google.")
            print("You can only hold one share in Google.")
            print(f"Google is trading at €{google} today.")
            print(f"€{google} has been added to your current account instead.")
            go_back_key()
        else:
            self.stocks += float(google)
            self.google += float(google)
            print("Congratulations, You have just won a share in google!")
            go_back_key()


def stock_quiz():
    """
    This Functions asks the users a series of questions. The questions are
    itterated through one by one
    prompting the user to give an answer. If the answer is correct the score is
    increased by one.
    If the user gets 100% of the questions right they will 1 share of google
    stock
    """
    clear()

    print("<------------------Stock Market Quiz--------------------->")
    print("\n<--Answer all questions right and win a share in google-->\n")
    forward_key()

    questions = (
        "What is the Stock Market? \n",
        "What do the bear and the bull stand for? \n",
        "Which statement about blue chips stocks is correct? \n",
        "What does 'Short Selling' mean? \n",
    )
    options = (
        (
            "A. The Stock Market is a market where people bet on race horses"
            " \nto gain some money.",
            "B. The Stock Market is a market where people buy products which"
            " \nthe merchants have a lot of stock of ",
            "C. The Stock Market is a market where people can buy stocks which"
            " \nare shares of companies.",
        ),
        (
            "A. The bear means stocks are falling and the bull means stocks"
            " \nare going up.",
            "B. They are signs that the Stock Market is opened and closed.",
            "C. The bear means stocks are rising and the bull means stocks are"
            " \nfalling.",
        ),
        (
            "A. Earnings are used for reinvestment in order to maintain the"
            " \ngrowing trend of the stocks",
            "B. The stocks are consistently profitable with a dividend"
            " \npayment",
            "C. They are traded below its market price",
        ),
        (
            "A. Selling securities that the investor has borrowed and prepared"
            " \nto buy back later at a lower price",
            "B. An trading strategy used to profit from a price decline",
            "C. Both A and B",
        ),
    )

    answers = ("C", "A", "B", "C")
    score = 0
    question_num = 0

    for question in questions:
        print("<---------- Stock Quiz ---------->\n")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("\nEnter (A, B or C) \n").upper()
        if guess == answers[question_num]:
            score += 1
            clear()
            print("Your last answer was correct!\n")
            forward_key()
        else:
            clear()
            print("Your last answer was inccorect!\n")
            forward_key()
        question_num += 1
    clear()
    print("---------------------------")
    print("          Results          ")
    print("---------------------------")

    score = int(score / len(questions) * 100)
    print(f"You scored: {score}% in the quiz!")
    if score == 100:
        initial_balance.quiz_prize()
    else:
        print("Unfortunaitly you didnt win a share in google today :(\n")
    go_back_key()


def forward_key():
    while True:
        forward = input("Enter 'c' to continue:\n").lower()
        if forward != "c":
            print("Not a valid option!\n")
            continue
        else:
            clear()
            break


def go_back_key():
    """
    Generic function that prompts user to enter a key to be returned to"
    "main menu
    """
    while True:
        back_key = input("\nPress b to return to main menu:\n").lower()
        if back_key == "b":
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
            crypto_buy_menu()

def check_balance_menu():
    """
    A menu that allows the user a choice of which balance they want to check
    """
    clear()
    print("<--------------------------->")
    print("     Account Balance Menu    ")
    print("<--------------------------->\n")
    print("1. Current Account Balance")
    print("2. Savings Account Balance")
    print("3. Stock Portfolio Balance")
    print("4. Crypto Portofolio Balance")
    print("5. Main Menu")
    choice = input("Please choose between options 1 - 5:\n")
    while True:
        if choice == "1":
            initial_balance.current_balance()
        elif choice == "2":
            initial_balance.savings_balance()
        elif choice == "3":
            initial_balance.stock_balance()
        elif choice == "4":
            initial_balance.crypto_blanance()
        elif choice == "5":
            main_menu()
        else:
            check_balance_menu()


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
            crypto_sale_menu()


def stock_buy_menu():
    """
    A menu that gives the user an option 3 stocks to purchase"
    """
    clear()
    print("Warning! Trading in stocks can be high risk but can come with high"
          " rewards!")
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
            stock_buy_menu()


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
            investment_menu()


def main_menu():
    """
    Systems main default menu designed for navigation around the banking
    application
    """
    clear()
    print("<--------------------------------->")
    print(" Welcome to Sheeran's Credit Union ")
    print("<--------------------------------->\n")
    print("<--------------------------------->")
    print("            Main Menu            ")
    print("<--------------------------------->\n")
    print("1. Check Balance")
    print("2. Deposit to Current Account")
    print("3. Withdraw Money")
    print("4. Deposit to Savings")
    print("5. Investment Menu")
    print("6. Investment Sales")
    print("7. Check Account Information")
    print("8. Quiz")
    print("9. Log out")
    choice = input("Please choose between options 1 - 8:\n")

    while True:
        if choice == "1":
            check_balance_menu()
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
            stock_quiz()
        elif choice == "9":
            print("Thank you for stopping by we hape to see you again soon!")
            quit()
        else:
            main_menu()


# Start up menu screen
print("<--------------------------------->")
print(" Welcome to Sheeran's Credit Union ")
print("<--------------------------------->\n")
print("<------------------------------->")
print(" Please fill in all details and \n register a new account with us ")
print("<------------------------------->\n")

forward_key()

# Pormpt The user to enter there details one at a time and check if charicters
# entered are correct
while True:
    fname = input("Please enter your first name:\n")
    if not fname:
        print("No Data Entered\n")
        continue
    if (
        num_check.search(fname) is None
        and special_character_check.search(fname) is None
    ):
        break
    else:
        print("\nNo special characters or numbers are allowed.")
        print("Please enter a valid first name.\n")
        continue
clear()
while True:
    lname = input("Please enter your last name:\n")
    if not lname:
        print("No Data Entered\n")
        continue
    if (
        num_check.search(lname) is None
        and special_character_check.search(lname) is None
    ):
        break
    else:
        print("\nNo special characters or numbers are allowed.")
        print("Please enter a valid last name.\n")
        continue
clear()
while True:
    try:
        age = input("Please enter your age:\n")

        if not age:
            print("No Data Entered\n")
            continue
        if char_check.search(age) is None and \
                special_character_check.search(age) is None:
            age = int(age)
            if age < 18:
                print("\nYou must be over 18 to have a Bank Account with us.\n")
                continue
            else:
                break
        else:
            print("\nNo special characters or letters are allowed.")
            print("Please enter a valid age.\n")
            continue
    except ValueError:
        print("\nNot a valid entry\n")
        continue


clear()
while True:
    country = input("Please enter what country do you reside in:\n")
    if not country:
        print("No Data Entered\n")
        continue
    if (
        num_check.search(country) is None
        and special_character_check.search(country) is None
    ):
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
        print("Please enter a valid Email\n")
        continue
clear()

# Random 4 digit number is assigned to the user for their account number
account_num = random.randint(999, 9999)

# User entered information is passed to User class
entered_info = User(fname, lname, age, country, email, account_num)
entered_info.account_created()

# User promted to enter an intial amount to their bank balance
while True:
    try:
        balance = input("Please enter an amount for your initial deposit:\n").lower()

        if not balance:
            print("No deposit entered!\n")
            continue
        if (
            char_check.search(balance) is None
            and special_character_check.search(balance) is None
        ):
            break
        else:
            print("\nNo special characters or letters are allowed.\n")
            continue
            clear()
    except ValueError:
        print("\nNot a valid entry\n")
        continue


# Add Values to bank and pass data back to initial deposit with balance amount
initial_balance = BankAccount(fname, lname, age, country, email, account_num,
                              balance)
initial_balance.initial_deposit()
main_menu()
