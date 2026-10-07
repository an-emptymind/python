import random

print("Welcome to Matermind")
secret = random.randint(1000, 9999)
secrets=list(str(secret))
print(secrets)
won=False
new_secrets=secrets.copy()

for i in range(0,6):
    black_peg=0
    white_peg=0
    try:
        guess=int(input("Guess the four digit number: "))
        guesses= list(str(guess))
        print(guesses)
    except ValueError:
        print("Invalid entry")
        continue
    for g in range(len(guesses)):
        used=[]
        if guesses[g] == secrets[g]:
            black_peg+=1
            used.append(g)
            new_secrets.pop(g)
            print(f"used:{used}")
            print(f"NewSec: {new_secrets}")
            print(f"if Index:{g}")
        elif guesses[g] in new_secrets and g not in used:
            print("in")
            white_peg+=1
            print(f"else Index:{g}")
    print(f"{black_peg} black pegs & {white_peg} white pegs")
    if black_peg==4:
        won=True
        print(f"You won. The secret is {guess}")
        break
    used=[]

if won == False:
    print("You lost")


        
