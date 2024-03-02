
import random
import time
blankboard = [' '] * 10

while True:
    #choose the character(PLAYER ONLY)
    option = input("Enter your character(X/O): ").title()
    if option == "X":
        player = "X"
        bot = "O"
        break
    elif option == "O":
        player = "O"
        bot = "X"
        break
    else:
        print("Invalid Option, Please enter again! ")
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
    EXPERIMENTAL VERSION:
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
            if user in range(1,10):
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
    # Check row
    if board[1] == board[2] == board[3] == player or board[4] == board[5] == board[6] == player or board[7] == board[8] == board[9] == player:
        return True
    elif board[1] == board[2] == board[3] == bot or board[4] == board[5] == board[6] == bot or board[7] == board[8] == board[9] == bot:
        return True
    # Check column
    elif board[1] == board[4] == board[7] == player or board[2] == board[5] == board[8] == player or board[3] == board[6] == board[9] == player:
        return True
    elif board[1] == board[4] == board[7] == bot or board[2] == board[5] == board[8] == bot or board[3] == board[6] == board[9] == bot:
        return True
    # Check cross
    elif board[1] == board[5] == board[9] == player or board[7] == board[5] == board[3] == player:
        return True
    elif board[1] == board[5] == board[9] == bot or board[7] == board[5] == board[3] == bot:
        return True
    #Tie
    elif ' ' not in board[1:9]:
        return False


def bot_interface():
    # Check the available slot
    available_slot = []
    for i in range(1,10):
        if blankboard[i] == ' ':
            available_slot.append(i)
    

    if not available_slot:
        return
    
    # Bot main mechanism
    bot_option = random.choice(available_slot)

    # Bot stop when it win(fix the previous bug)
    if win_condition(blankboard):
        return True
    else:
        blankboard[bot_option] = bot

def main():
    count = 0
    print("\nBot's Character:",bot)
    print("Player's Character:",player)


    for i in range(1,10):
        count = count + 1
        print("Loading...\n")
        time.sleep(1)
        print(f"""\n
              =================
              | Turn: {count} |
              =================""")
        print_board(blankboard)
        user_interface()
        bot_interface()        

        if win_condition(blankboard) == True:
            print_board(blankboard)
            print("We have a winner")
            break
        elif win_condition(blankboard) == False:
            print_board(blankboard)
            print("Draw!!")
            break
        
        switchTurn()
if __name__ == "__main__":
    main()

    

