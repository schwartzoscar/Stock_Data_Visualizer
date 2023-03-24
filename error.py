# This file should error check every possible error
import re

def CheckSymbolInput(x):
    pattern = r"^[A-Z]{1,5}$"
    if not re.match(pattern, x):
        print("Invalid input. Input is not a valid stock code.")
        return False
    else:
        return True
