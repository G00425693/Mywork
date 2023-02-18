# need to use a string to input a 10 digit account number and output the answer with xs and only the lasts 4 digits displaying
# Author: Audrey Fitzgerald
# learning slicing []

a = "xxxxxxxxx"
# a is a string of x's
b = input('Please enter your account number:')
print(a[0:5] + b[5:9])
