#Michael Briggs
#0456918
#09/08/19
#MSITM 6341

stock_symbol = "aapl"
price = 204.66
yesterdays_price = 200.58
dollar_amount_changed = yesterdays_price-price

print("Symbol: " + stock_symbol.upper() + ", Price: " + str(price) + ", Change: " + str(round(dollar_amount_changed, 2)))
print("\n\n")
print("Symbol: " + stock_symbol + ", Price: $" + str(price) + ", Change: " + str(round(dollar_amount_changed, 2)))
print("\n\n")
print("Symbol: " + stock_symbol.upper() + "---" + "Yesterday's Price: " + str(yesterdays_price))