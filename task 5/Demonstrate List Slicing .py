"""Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
#list
number=list(range(1,11))
print(number)
#first five
first_five=number[0:5]
print(first_five)
#reverse
first_five.reverse()
print (first_five)
