import random
import re
import os

def clear():
    # check if operating system is mac and linux or windows.
    if os.name == 'posix':
        _ = os.system('clear')

    else:
        # else operating system is windows
        _ = os.system('cls')
