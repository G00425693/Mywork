#this programme will take in an integer and output a float rounded down
# Author: Audrey Fitzgerald
# need to use math module math.floor() maths is a built in module

import math

numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))

