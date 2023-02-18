#Q 6 message = 'I have eaten ' + 99 + ' burritos.'
#print (message)

#this will not work as you can only concantenate str (not "int") to str

message = "I have eaten "  + str("99") +  " burritos."
print (message)

#made error in python output by forgetting the s in questions...
#needed to put in spaces to get the sentence to print correctly

#Q 7 Why is eggs a valid variable name while 100 is invalid?
# as per W3schools you cannot start a variable with a number
# •	Variable names must start with a small letter, they cannot start with an integer

#Q 8 What three functions can be used to get the integer, floating-point number, or
# string version of a value?
# int()
# float()
# str()
# info capatured from chart in week 3 lession
