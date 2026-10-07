import random
words = ["apple", "brave", "crane", "flame", "ghost", "plant"]
secret = random.choice(words)
won = False
new_word=""

for r in range(6):
    
    guess = input("Guess the five letter word : ")
    if len(guess) == 5 and guess.isalpha():
        print("")
    else:
        print("Invalid word")
        continue
    secret_letters = set(secret)
    for i in range(5):
        if guess[i] == secret[i]:
            new_word+= "*"
        elif guess[i] in secret_letters:
            new_word+= "&"
        else:
            new_word+=guess[i]
    print(f"Secret letter: {new_word}")
    if new_word=="*****":
        print("You won")
        won=True
        break
    new_word=""
if won==False:
    print(f"You lost, The word was {secret}")
