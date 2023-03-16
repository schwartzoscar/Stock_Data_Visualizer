import requests
#This file should handle all of the api interactions and be able to return values to other files
#def main():
    #return

url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=ARJ4YHDD7BSSD94B'
r = requests.get(url)
data = r.json()

print(data)
#key = "ARJ4YHDD7BSSD94B"
#main()