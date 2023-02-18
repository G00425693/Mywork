# lesson on printing out random list of fruits
# Author: Audrey Fitzgerald
# q5 week 3

import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]

# i want to print a random fruit from the list above not sure what the numbers have to do with it
index = random.randint(0,len(fruits)-1) #returned error message as I didn't define index 
print("A Random Fruit:{}".format(fruit))
# error I made on this intially is I had index on line before fruits, think of order of what your doing
