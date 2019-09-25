#Michael Briggs
#0456918
#09/29/2019
#MSITM 6341

menu_items_in_stock = ['Tacos', 'Chips', 'Salsa', 'Quesadilla']
customer_order = ['Tacos', 'Guacamole', 'Burrito', 'Chips', 'Salsa']

menu_items_in_stock = [item.lower() for item in menu_items_in_stock]
customer_order = [item.lower() for item in customer_order]

for item in customer_order:
    if item in menu_items_in_stock:
        print("We have " + item.title() + " in stock.")
    else:
        print("We do not have " + item.title() + " in stock.")
