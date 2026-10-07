import random

board = ["","","","","","","","",""]
print("Welcome to Tic-Tac-Toe")
print("You need to enter the index of place you want to fill")
print(" 0 | 1 | 2\n ---------\n 3 | 4 | 5\n ---------\n 6 | 7 | 8")

def print_table(board):
    temp_board = board.copy()
    for b in range(len(temp_board)):
        if temp_board[b] == "":
            temp_board[b] = b
    print(f" {temp_board[0]} | {temp_board[1]} | {temp_board[2]}\n ---------\n {temp_board[3]} | {temp_board[4]} | {temp_board[5]}\n ---------\n {temp_board[6]} | {temp_board[7]} | {temp_board[8]}")

def bot_play(board):
    rem=[]
    for i in range(len(board)):
        if board[i]=="":
            rem.append(i)
    choice= random.choice(rem)
    return choice

def check_winner(board):
    winner_tuples= [(0,1,2), (3,4,5), (6,7,8),(0,3,6), (1,4,7), (2,5,8),(0,4,8), (2,4,6)]
    bot_choices=[]
    user_choices=[]
   
    for i in range(len(board)):
        if board[i] == "x":
            user_choices.append(i)
        elif board[i] == "o":
            bot_choices.append(i)
    #print(f"Bot choices:{bot_choices}")
    #print(f"User choices: {user_choices}")

    for winner in winner_tuples:
        if all(num in user_choices for num in winner):
            return 0

        if all(num in bot_choices for num in winner):
            return 1
    if len(user_choices) + len(bot_choices) >= 9:
        return 2
    
    return 3

def bot_play_v2(board):
    played = False
    for b in range(len(board)):
        if board[b] == "":
            board[b] = "o"
            result = check_winner(board)
            board[b] = ""
            if result == 1:
                played = True
                return int(b)
            

    for b in range(len(board)):
        if board[b] == "":
            board[b] = "x"
            result = check_winner(board)
            board[b] = ""
            if result == 0:
                board[b] = "o"
                played = True
                return int(b)    
    
    if played == False:
        result = bot_play(board)
        return result


ttt = False

while ttt == False:
    try:
        user_choice=int(input("Enter your choice:"))
    except ValueError:
        print("Invalid choice")
        continue
    if user_choice < 0 or user_choice > 8 or board[user_choice] != "":
        print("Invalid or taken cell, try again")
        continue
    board[user_choice] = "x"
    print_table(board)
    result = check_winner(board)
    if result == 0:
        print("User wins")
        ttt= True
        break
    elif result == 1:
        print("Bot Wins")
        ttt= True
        break
    elif result == 2:
        ttt= True
        print("Its a draw!")
        break
    bot_choice = bot_play_v2(board)
    board[bot_choice] = "o"
    print(f"Bot chooses: {bot_choice}")
    print_table(board)
    result = check_winner(board)
    #print(f"Result:{result}")
    if result == 0:
        print("User wins!")
        ttt= True
    elif result == 1:
        ttt= True
        print("Bot wins")
    elif result ==2:
        ttt= True
        print("Its a draw!")




    




