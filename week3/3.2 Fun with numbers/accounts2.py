#modifying accounts py to display x's for infinite numbers apart from last 4 digits
# used w3 schools and google educative.io for assistance
# Author: Audrey Fitzgerald


# a is a string of x's
b = input('Please enter your account number:')
#c is the amount of numbers in b
c = (len(b))
a = (c*("x"))
print(a[0:c-4] + b[c-4:c])