# using random and tuples
# Audrey Fitzgerald
# this program should print out a random fruit
import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')
#note tuple is in rounded brackets
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))
