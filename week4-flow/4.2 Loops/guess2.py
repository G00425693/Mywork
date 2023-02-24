# using while and if loops
# Audrey Fitzgerald
# informing the user if their guess was to high or to low

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
        guess = int(input("Please guess again:"))
    else: # I know it cant be equal or too low, so it must be too high
        print("too high")
        guess = int(input("Please guess again:"))
else:
    print("Well done! Yes the number was ", numberToGuess)