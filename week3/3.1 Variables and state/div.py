# dividing week 3 question 3 lesson
# Author: Audrey Fitzgerald
# programme that inputs two numbers 
# outputs integer and remainder

x = int(input("enter the first number:"))
y = int(input("enter the number you want to divide by:"))
answer = (x//y) #// means it will return answer as an integer (leaned from sololearn and this lesson)
remainder = x%y # % gives the remainder, still confused as to why not in brackets this time..

print("{} divided by {}") # my first attempt at doing it myself 

print("{} divided by {} is {} with remainder {}".format( x, y,
answer, remainder)) ~copied from lecture 
print ("{} divided by {} with remainder {}".format(x,y, answer, remainder)) #my attempt left out is!! and set of {}




