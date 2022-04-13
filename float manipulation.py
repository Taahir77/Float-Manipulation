
# imports additional maths functions

import math

# empty list

mylist = []

# for loop with a maximum range of 10
# user asked to enter 10 decimal point numbers 
# variable casting from a string to a float applied
# user inputs then get stored the "mylist" list
# all the numbers in the list then displayed

for i in range(10):

   mylist.append(float(input("enter 10 decimal numbers: ")))
        
print("All the numbers in the list are:", mylist)
  
# "add" variable sums up all the numbers in the "mylist" list
# sum function used

add = sum(mylist)
print("the sum of mylist is:", add)

# "max_value" variable gives the number with the highest numerical value in the list
# max function used

max_value = max(mylist)
print("The maximum number is:", max_value)

# "min_value" variable gives the number with the lowest numerical value in the list
# min function used

min_value = min(mylist)
print("The minimum number is:", min_value)

# "n" variable is the number of items in the list
# this is determined by the range = 10

n = 10 

# the average average of the list is the sum of the all the numbers in the list (sum) divided by the number of item in the list (n) 
# displays the average rounded off to two decimal places

avg_value = add / n
print("the average is:", round(avg_value, 2))

# the sort function sorts all the numbers in the list from smallest to largest
# this needs to be done in order to determine the mean
# we know the number of items in the list is 10, which is even
# we then know that the two middle numbers are summed and then divided by 2 in order to get the median of the list
# the median is then displayed

mylist.sort()
median = (mylist[4]+ mylist[5])/2
print("The median of the list is:", median)

