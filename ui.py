import graph
import api
import error
import app
while True:
    print("Stock Data Visualizer\n--------------------")
    stockSymbol = input("Enter the stock Symbol you are looking for: ")
    print(stockSymbol)
    #CHECK IF SYMBOL IS VALID USING error.py
    
    valid_chart_type = False
    while not valid_chart_type:
        chartType = input("Chart Types\n----------\n1. Bar\n2. Line\nEnter the chart type you want (1, 2): ")
        if chartType == '1':
            print("Bar")
            valid_chart_type = True
        elif chartType == '2':
            print("Line")
            valid_chart_type = True
        else:
            print("Invalid input. Please enter 1 or 2.")

    valid_time_type = False
    while not valid_time_type:
        timeSeries = input("Select the time series of the chart you want to generate\n--------------------------\n1. Intradaily\n2. Daily\n3. Weekly\n4. Monthly\nEnter the time series option (1, 2, 3, 4): ")
        if chartType == '1':
            print("Intradaily")
            valid_time_type = True
        elif chartType == '2':
            print("Daily")
            valid_time_type = True
        elif chartType == '3':
            print("Daily")
            valid_time_type = True
        elif chartType == '4':
            print("Weekly")
            valid_time_type = True
        else:
            print("Invalid input. Please enter 1, 2, 3 or 4.")
    
    restart = input("Do you want to restart the program? (y/n): ")
    
    if restart.lower() != 'y':
        break

# This document contains functions to create the user interface

# It should take input and call the functions in error.py to check if it is valid

# It should then send the user data to the functions in api.py
