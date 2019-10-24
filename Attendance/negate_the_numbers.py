#Michael Briggs
#0456918
#10/29/2019
#MSITM 6341

#Problem of the day 2
#Create a list of randomly chosen numbers and write a loop that negates all of the numbers on the list
#I'm assuming that means make the numbers 0 through subtraction
numbers = [1,3,5,7,8,408,65,76,87,99,11,21,32,23]
print(numbers)

#Loop will replace each item in the list with that number minus itself
idx = 0
for value in numbers:
    numbers[idx] = value - value
    idx = idx +1 

print(numbers)
    
