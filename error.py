# This file should error check every possible error
def CheckSymbolInput(x):
    count = 0
    for char in x:
        if count > 5:
            print("Invalid Input. Too many characters in input, make sure to NOT include $")
            return False
        else:
            count += 1
            return True
        