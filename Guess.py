import random

target = random.randint(1, 100)

while True:
    userGuess = input("Enter your guess: ")
    if(userGuess == "Q"):
        break

    userGuess = int(userGuess)
    if(userGuess == target):
        print("Congratulations! You got it!")
        break
    elif(userGuess < target):
        print("Too low!")
    else:
        print("Too high!")


print("Game over!")
