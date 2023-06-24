import random
import re
import os

def clear():
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