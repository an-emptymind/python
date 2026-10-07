import random

choices = {0:"Rock",1:"Paper",2:"Scissor"}

def start_game():
    print("Welcome to Rock Paper scissor game")
    print("Its best of 5. First player to win 3 matches wins!")
    user_score=0
    bot_score=0
    m=0
    game_over = False
    while m <5:
        try:
            user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper & 2 for Scissor\n"))
        except ValueError:
            print("Please enter a number (0, 1, or 2)")
            continue
        if user_choice not in choices:    # ← rejects 5, -1, 99, etc.
            print("Invalid choice, pick 0, 1, or 2")
            continue
        print(f"You chose: {choices[user_choice]}")
        bot_choice = random.randint(0,2)
        m+=1
        print(f"Bot chose: {choices[bot_choice]}")
        if user_choice == bot_choice:
            print("Tie")
        elif user_choice == 0:
            if bot_choice == 1:
                bot_score+=1
            else:
                user_score+=1
        elif user_choice == 1:
            if bot_choice == 0:
                user_score+=1
            else:
                bot_score+=1
        elif user_choice == 2:
            if bot_choice == 0:
                bot_score+=1
            else:
                user_score+=1
        print("-------------------------")
        print(f"User score: {user_score}")
        print(f"Bot score: {bot_score}")
        print("-------------------------\n")
        if user_score == 3 or bot_score == 3:
            if user_score == 3:
                print("You win")
            else:
                print("You lose")
            game_over = True
            break

    if game_over == False:
        if user_score > bot_score:
            print("You win!")
        elif user_score == bot_score:
            print("It's a tie!")
        else:
            print("You lose!")

    
    print("Thank you")

start_game()