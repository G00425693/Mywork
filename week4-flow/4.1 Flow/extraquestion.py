#while loops 
#author: Audrey Fitzgerald
# while condition:
#   statements

# what the user to enter a number until they reach -1 after which point the programme should stop

a = 0   #variable number is set to 0 meaning the user can enter any number
while a != -1:  # the while condition in this instance is set to -1 as it is the cut off to quit
    a = int(input("Enter a number : "))  #we require the user to input any number positve or negative and once they pick-1 it stops
    print(a)

#don't forget to indent after the while command