import random

def guess_the_number():
    number = random.randint(1, 100)
    print("Lets start the game")
    right_guess = False
    count=0
    while right_guess == False:
        try:
            guess = int(input("Guess a number between 1 to 100:"))
        except ValueError:
            print("Please type a number!")
            continue
        count+=1
        if guess > 100 or guess < 0 :
            print("Invalid number,try again")
        elif guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        elif guess == number:
            print("Congrats, Your guess is right!")
            print(f"You did it in {count} attempts")
            right_guess = True            


guess_the_number()