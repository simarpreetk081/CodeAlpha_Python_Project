stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 130
}

print("Stock Portfolio Tracker")

stock = input("Enter Stock Name: ").upper()

if stock in stocks:
    quantity = int(input("Enter Quantity: "))

    total = stocks[stock] * quantity

    print("Stock Price:", stocks[stock])
    print("Total Investment:", total)

else:
    print("Stock Not Found")