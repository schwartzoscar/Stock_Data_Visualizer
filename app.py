import ui
import graph
import api
import error

api = None
stockSymbol = None
chartType = None
timeSeries = None
bDate = None
eDate = None

#Main function needs to accept input and send output to the ui.py file.
def Main():
    #Call function in ui.py that begins the interaction between the user and system
    #ui.[functionname]()
    return

########################
#This is the Set Section
#These are things/functions for me to grab information
########################

def SetApi(x):
    #Gets Api key from api.py 
    global api
    api = x

def SetStockSymbol(x):
    #Gets input from UI and sets the stock symbol
    global stockSymbol
    stockSymbol = x

def SetChartType(x):
    #Gets input from UI to determine the chart that they would like to use
    global chartType
    chartType = x

def SetTimeSeries(x):
    #Gets input from UI and chooses a time series
    #Intraday, Daily, Weekly, Monthly
    global timeSeries
    timeSeries = x

def SetBeginningDate(x):
    #Gets input from UI to set the beginning date for the charts
    #Must be a correct formart (error check)
    global bDate
    bDate = x

def SetEndDate(x):
    #Gets input from UI to set the end date for the charts
    #Must be a correct formart (error check)
    #Cannot be before the beginning date (error check)
    global eDate
    eDate = x 

########################
#This is the Get Section
########################
#To use these functions from other files (dont type the quotation marks):
#You must have "import app" in the beginning of you file, like mine does
#Then when calling the function you just type it with "app.functionname(parameter)"
########################
def GetApi():
    #Returns the api key
    return api

def GetStockSymbol():
    #Returns the stock symbol
    return stockSymbol
    
def GetChartType():
    #Returns the chart type
    return chartType

def GetTimeSeries():
    #Returns the chosen time series
    #Intraday, Daily, Weekly, Monthly
    return timeSeries

def GetBeginningDate():
    #Returns the beginning date
    #Must be a correct formart (error check)
    return bDate

def GetEndDate():
    #returns the end date
    #Must be a correct formart (error check)
    #Cannot be before the beginning date (error check)
    return eDate

Main()