#1. Write a program called round.py. The program should take in a float and
#output an int (rounded up or down)
# Author: Audrey Fitzgerald
# rounds, rounds to nearest even number so is not an accurate indicator 
# I want to round flat 5.99 to 6
# error I made was entered the float number into the programme


numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))