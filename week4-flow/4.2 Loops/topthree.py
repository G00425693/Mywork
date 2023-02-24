# program is to generate 10 numbers and print the top 3
# random module needs to be imported
# Author: Audrey Fitzgerald

import random

howMany = 10 # want the program to generate 10 numbers
topHowMany = 3 # want it to print out the top 3
rangeFrom = 0
rangeto = 100
numbers = []


for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeto))
print (f"{howMany} random numbers\t {numbers}")
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print (f"The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")
#f function was missing from the
