import random

def build_word(guess,secret,temp_word):
    for i in range(len(secret)):
        if guess == secret[i]:
            temp_list = list(temp_word)
            temp_list[i]= guess
            new_word= "".join(temp_list)
            temp_word=new_word
    return new_word

def guess_game():
    words = ["python", "banana", "coffee", "guitar", "rocket"]

    secret = random.choice(words)

    won = False
    Life =6
    guessed=[]
    temp_word="_" * len(secret)

    while won == False :
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue
        if guess in guessed :
            print("Already guessed this letter")
        else:
            if guess in secret :
                guessed.append(guess)
                temp_word = build_word(guess,secret,temp_word)
                print("Correct")
                print(f"Word is : {temp_word}")
                if temp_word == secret:
                    print("You won!")
                    break
            else:
                guessed.append(guess)
                Life-=1
                print(f"wrong, life remianing {Life}")
                if Life<1:
                    print("You lost")
                    break


guess_game()