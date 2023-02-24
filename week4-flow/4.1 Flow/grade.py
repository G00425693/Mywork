# 2. this program should read in a students % and print out the grade
# author: Audrey Fitzgerald

percentage = float(input("Enter the percentage: "))
#print (percentage)

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 39.5: 
    print ("Fail")
elif percentage < 49.5: 
    print ("Pass")
elif percentage <59.5:
    print ("Merit1")
elif percentage <69.5:
    print ("Merit2")
else: print ("Distinction")

# Q3 extra question, motify the program to round up a %
# way I have done this is to modify each of the grades by 0.5%

# Q4 How would you use a while loop to modify 1 so that it keeps prompting the
#user for a number until the user enters -1


