# messing with lists
# Author: Audrey Fitzgerald
# need to import random to answer this question

import random # asking the program to pick random numbers 
queue = [] # is a list
numberOfNumbers=10  #want the list to pick 10 numbers
rangeTo=100  

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print (f"queue is {queue}")

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print (f"current Number is:{currentNumber} and the queue is: {queue}") #remember the f and to indent the print for the while loop
print ("the queue is now empty")