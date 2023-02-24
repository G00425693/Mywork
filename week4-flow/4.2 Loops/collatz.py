# asks the user to input a positive integer and outputs as per calcuation below
# At each step calculate the next value by taking the current value and, if it is even
# divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one
# Author - Audrey Fitzgerald

# num = (num % 2) == 0 # A number is even if division by 2 gives a remainder of 0
# num = (num % 2) == 1  # If the remainder is 1, it is an odd number.

#num >=1  # number should not be less than 1 but can be anything greater
#num = int(input("Enter a number: "))
#num == 0
#if True:
#   print (num/2)
#else:
#   print(num (*3+1))
#   if num != 1
#   continue
#print 
num = int(input("Enter a number: "))
while num > 1:  #put this in so sequence would stop at 1
   if num % 2 == 0:  
      num //= 2
      print(num)
   else:
      num = (num * 3) + 1  # == was preventing the program from running
      print(num)