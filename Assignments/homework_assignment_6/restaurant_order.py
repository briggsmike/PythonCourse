#Michael Briggs
#0456918
#10/22/2019
#MSITM 6341

#menu dictionary
restauraunt_menu = {
    'chicken':10,
    'mashed potatoes':5,
    'eggs':2,
    'milk':1.5,
    'salad':6,
}

#customer order list
customer_order = ['chicken','pork','mashed potatoes','salad','root beer','eggs']

#total cost variable
total_cost = 0

#loop that will determine if an ordered item from the list is in the dictionary
#and will provide the price of available items in the customer order
for item in customer_order:
    if item in restauraunt_menu:
        print(item.title() + ": $" + str(float(restauraunt_menu[item])))
        total_cost = total_cost + restauraunt_menu[item]
    else:
        print("We do not have " + item.title())

#formatting
print("--------------------")

#print the total cost
print("Order total: $" + str(float(total_cost)))