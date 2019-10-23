#Michael Briggs
#0456918
#10/22/2019
#MSITM 6341

#Problem of the day
#Create a list of numbers chosen randomly by myself and write a loop to find the largest element in the list

numbers = [1,3,5,7,8,408,65,76,87,99,11,21,32,23]
#easy method
#print(max(numbers))

#using a loop
greatest = 0
for value in numbers:
    if value > greatest:
        greatest = value 
print(greatest)
