import time

blankboard = [' '] * 10
player = "O"

def switchPlayer():
    global player
    if player == "X":
        player = "O"
    
    else:
        player = "X"
    return player

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

    Current player: {player}
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
                print("Please enter a number from 1-9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    blankboard[user] = player


def win_condition(board):
    # Check row
    if board[1] == board[2] == board[3] == player or board[4] == board[5] == board[6] == player or board[7] == board[8] == board[9] == player:
        return True
    # Check column
    elif board[1] == board[4] == board[7] == player or board[2] == board[5] == board[8] == player or board[3] == board[6] == board[9] == player:
        return True
    # Check cross
    elif board[1] == board[5] == board[9] == player or board[7] == board[5] == board[3] == player:
        return True
    #Tie
    else:
        return False


def main():
    count = 0
    print(player)
    for i in range(1, 10):
        count = count + 1

        print(f"\nTurn {count}")
        print_board(blankboard)
        user_interface()
        win_condition(blankboard)
        if win_condition(blankboard) == True:
            print_board(blankboard)
            print(f"PLAYER {player} won!!!!")
            break
        else:
            if count == 9:
                print_board(blankboard)
                print("DRAW!!")
        switchPlayer()
if __name__ == "__main__":
    main()

