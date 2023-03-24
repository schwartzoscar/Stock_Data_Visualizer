# This file should error check every possible error
def CheckSymbolInput(x):
    count = 0
    for char in x:
        count += 1
    if not char.isalnum():
        print("Invalid Input. Input contains special characters.")
        return False
    if count > 5:
        print("Invalid Input. Too many characters in input, make sure to NOT include $")
        return False
    else:
        return True
        
