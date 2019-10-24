#Michael Briggs
#0456918
#10/29/2019
#MSITM 6341

#Problem of the day 2
#How would you compute the length of a list without the ability to use len()

numbers = [1,3,5,7,8,408,65,76,87,99,11,21,32,23,24,5,6,7,8,6,5,4,34,5,6]
print("\nThe list of numbers:")
print(numbers)

idx = 0
for value in numbers:
    idx = idx + 1

print("\nThe number of values in the list according to len() is: " + str(len(numbers)))
print("The number of values in the list according to my method is: " + str(idx) + '\n')