#Michael Briggs
#0456918
#10/29/2019
#MSITM 6341

#Problem of the day 1
#Sum N number of even numbers and output the result. Assume you are given a random list of numbers that could
#be a mix of odd and even numbers.

numbers = [11,22,33,44,55,66,77,88,99,12,23,34,45,56,67,78,89]
even_numbers = []

for value in numbers:
    if value % 2 == 0:
        even_numbers.append(value)

print("Random list of numbers:")
print(numbers)
print("Just the even numbers:")
print(even_numbers)
print("The sum of all the even numbers:")
print(sum(even_numbers))