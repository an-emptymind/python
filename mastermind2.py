import random

print("Welcome to Matermind")
secret = random.randint(1000, 9999)
secrets=list(str(secret))
#print(secrets)

won=False

for i in range(0,10):
    black_peg=0
    white_peg=0
    new_secrets=secrets.copy()
    try:
        guess=int(input("Guess the four digit number: "))
        guesses= list(str(guess))
        new_guesses=guesses.copy()
        #print(new_guesses)
    except ValueError:
        print("Invalid entry")
        continue
    if len(guesses) != 4:
        print("Enter 4 digits")
        continue
    for g in range(len(guesses)):
        if guesses[g] == secrets[g]:
            black_peg+=1
            new_secrets.remove(guesses[g])
            new_guesses.remove(guesses[g])
            #print(f"New secrets:{new_secrets}")
            #print(f"New guesses:{new_guesses}")
    for h in range(len(new_guesses)):
        if new_guesses[h] in new_secrets:
            new_secrets.remove(new_guesses[h])
            white_peg+=1
            #print(f"Newest secret: {new_secrets}")

    print(f"{black_peg} black pegs & {white_peg} white pegs")
    if black_peg==4:
        won=True
        print(f"You won. The secret is {guess}")
        break

if won == False:
    print("You lost")