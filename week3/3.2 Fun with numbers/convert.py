# takes in a float amount of dollars and returns that
# absolute amount in cent.
# Author: Audrey Fitzgerald

import math

number = float(input("Please enter an amount:"))
absoluteValue = abs(number)
print('The amount entered in dollars is $ {}'.format(absoluteValue))
number2 = int(number*100)
print('The amount entered in cents is  {}'.format(number2), 'cents')

