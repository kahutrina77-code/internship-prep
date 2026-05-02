import random
def guessing_game():
    secret = random.randint(1, 100)
    guesses = 0

    print("I'm thinking of a number between 1-100")  

    while True:
        guess = int(input("guess a number: "))
        guesses = guess + 1

        if guess < secret :
            print("Too low!")
        elif guess > secret :
            print("Too high!") 

        else:
            print("guess was correct boo!", guesses)        

        break 

guessing_game()   