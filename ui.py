while True:
    print("Stock Data Visualizer\n--------------------")
    Symbol = input("Enter the stock Symbol you are looking for: ")
    print(Symbol)
    #CHECK IF SYMBOL IS VALID USING error.py
    
    valid_chart_type = False
    while not valid_chart_type:
        Chart_type = input("Chart Types\n----------\n1. Bar\n2. Line\nEnter the chart type you want (1, 2): ")
        if Chart_type == '1':
            print("Bar")
            valid_chart_type = True
        elif Chart_type == '2':
            print("Line")
            valid_chart_type = True
        else:
            print("Invalid input. Please enter 1 or 2.")
    
    restart = input("Do you want to restart the program? (y/n): ")
    
    if restart.lower() != 'y':
        break

# This document contains functions to create the user interface

# It should take input and call the functions in error.py to check if it is valid

# It should then send the user data to the functions in api.py
