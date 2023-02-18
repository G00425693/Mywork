#Write a program (absolute.py) that takes in number and give its absolute
#value (ie -4 or 4 would both output 4)
#Author: Audrey Fitzgerald
# question asks the number to be returned as a float

number = float(input("Please enter an amount:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))