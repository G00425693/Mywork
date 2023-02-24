#messing with flow
# Author: Audrey Fitzgerald 

name = (input("what is your name?"))


if name == "Alice":
    print("Hi Alice.")
    age = (int(input("what is your age?")))
    if age < 12:
        print("You are not Alice, kiddo.")
    elif age > 2000:
        print("Unlike you, Alice is not an undead, immortal vampire.")
    elif age >100:
        print("You are not Alice, grannie.")
    else:
        print("Welcome Alice!")
else:
    print("You are not Alice, kiddo.")
