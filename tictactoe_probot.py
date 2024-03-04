import time

blankboard = [' '] * 10

while True:
    # choose the character(PLAYER ONLY)
    option = input("Enter your character(X/O): ").title()
    if option == "X":
        player = "X"
        bot = "O"
        break
    elif option =="O":
        player = "O"
        bot = "X"
        break
    else:
        print("Invalid Input, Try again!")
        time.sleep(1)
# Switch Turn  
def switchTurn():
    global player,bot
    if player == "X":
        bot = "O"
    elif player == "O":
        bot = "X"
    
def print_board(board):
    print(f"""
    -------------------------------------------Board Interface -----------------------------------------------
    BEST VERSION(UNBEATABLE BOT):
                                                Instruction: Press the numbers 1 to 9 as shown in the table
    =======                                     =============   
    |{board[1]}|{board[2]}|{board[3]}|                                     | 1 | 2 | 3 |                                                                      
    =======                                     =============  
    |{board[4]}|{board[5]}|{board[6]}|                                     | 4 | 5 | 6 |
    =======                                     =============  
    |{board[7]}|{board[8]}|{board[9]}|                                     | 7 | 8 | 9 |
    =======                                     =============  

    ----------------------------------------------------------------------------------------------------------
    """)

def user_interface():
    while True:
        try:
            user = int(input("Enter a number from 1-9: "))
            if user in range(1, 10):
                if blankboard[user] == ' ':
                    blankboard[user] = player
                    break
                else:
                    print("The box already filled, Please provide another answer")
            else:
                print("Invalid index number, Please enter again! ")
        except ValueError:
            print("Invalid input, Please enter a valid number! ")

def win_condition(board):
    # check row:
    for i in range(1,8,3):
        if board[i] == board[i+1] == board[i+2] == player:
            return -1
        elif board[i] == board[i+1] == board[i+2] == bot:
            return 1
    # check column
    for i in range(1,4):
        if board[i] == board[i+3] == board[i+6] == player:
            return -1
        elif board[i] == board[i+3] == board[i+6] == bot:
            return 1
    # check diagonals
    if board[1] == board[5] == board[9] == player or board[3] == board[5] == board[7] == player:
        return -1
    elif board[1] == board[5] == board[9] == bot or board[3] == board[5] == board[7] == bot:
        return 1

    # check tie
    if ' ' not in board[1:10]:
        return 0
    
    return None

def bot_interface():
    bestScore = -1000
    bestmove = 0
    for i in range(1,10):
        if blankboard[i] == ' ':
            blankboard[i] = bot
            score = minimax(blankboard,0,False)
            blankboard[i] = ' '
            if score > bestScore:
                bestScore = score
                bestmove = i
    blankboard[bestmove] = bot


def minimax(board,depth,isMaximizing):
    score = win_condition(board)

    if score != None:
        return score
    
    if isMaximizing:
        bestScore = -1000
        for i in range(1,10):
            if board[i] == ' ':
                board[i] = bot
                bestScore = max(bestScore,minimax(board,depth + 1,False))
                board[i] = ' '
        return bestScore
    else:
        bestScore = 1000
        for i in range(1,10):
            if board[i] == ' ':
                board[i] = player
                bestScore = min(bestScore,minimax(board,depth + 1,True))
                board[i] = ' '
        return bestScore
    

   
def main():
    count = 0
    print("\nBot's Character:", bot)
    print("Player's Character:", player)

    for i in range(1, 10):
        count = count + 1
        print("Loading...\n")
        time.sleep(1)
        print(f"""\n
              =================
              | Turn: {count} |
              =================""")
        print_board(blankboard)

        if count % 2 == 1:
            user_interface()
        else:
            bot_interface()

        if win_condition(blankboard) != None:
            print_board(blankboard)
            if win_condition(blankboard) == 0:
                print("DRAW!!")
            elif win_condition(blankboard) == 1:
                print("Bot wins")
            else:
                print("Player wins!!")
            break

if __name__ == "__main__":
    main()