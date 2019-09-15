#Michael Briggs
#0456918
#09/15/2019
#MSITM 6341

groceries = ['milk','eggs','cheese','water','bread']
grocery_prices = ['2.38','1.89','1.19','3.33','2.22']

#I printed out what the code is doing for each step instead of just printing out the list values with no context

print("1. Print the 3rd item followed by it’s price: " + groceries[2] + ", " + grocery_prices[2])
print("2. Print the last item followed by it’s price: " + groceries[-1] + ", " + grocery_prices[-1])
print("3. Add a 6th item and it’s price. (Adding pasta for $4.41)")
groceries.append('pasta') 
grocery_prices.append('4.41')
print("4. Print the list of items: ")
print(groceries)
print("5. Print the list of prices: ")
print(grocery_prices)
print("6. Remove the first item and it’s price. (Removing milk and it's price of $2.38)")
del groceries[0]
del grocery_prices[0]
print("7. Double the price of the 2nd item. (Doubling the price of the new 2nd item, cheese $1.19)")
grocery_prices[1] = 2*float(grocery_prices[1])
print("8. Print the list of items: ")
print(groceries)
print("9. Print the list of prices: ")
print(grocery_prices)