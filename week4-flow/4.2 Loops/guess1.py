# while loops getting the user to guess a number untl they guess the correct one
# Author: Audrey Fitzgerald
# number to guesss is 30

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:   #spell guess correctly....
    print("Wrong")
    guess = int(input("Please guess again:"))

if guess == numberToGuess:   #needed an if statement as wasn't running as expected 
    print("Well done! Yes the number was", numberToGuess)