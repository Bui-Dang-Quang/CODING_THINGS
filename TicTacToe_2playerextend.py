while True:
    try:
        length = int(input("Length: "))
        if length > 2:
            break
        else:
            print("You should enter at least 3x3!!")
    except ValueError:
        print("Invalid input, please try again! ")

blankboard = []
for i in range (length):
    row = [' '] * length
    blankboard.append(row)

while True:
    # choose your roleplay
    option = input("Enter roleplay(X/O):").title()
    if option == "X":
        player = "X"
        break
    elif option == "O":
        player = "O"
        break
    else:
        print("Invalid Option")


# Switch turn
def switchPlayer():
    global player
    if player == "X":
        player = "O"
    
    else:
        player = "X"
    return player

def Board(board):
    for i in range (length):
        print("=="*length + "=")
        for j in range(length):
            print(f"|{board[i][j]}",end="")
        print("|")
    print("=="*length + "=")

def IndexBoardInfo(board):
    for i in range (length):
        print("======"*length + "=")
        for j in range(length):
            print(f"|({i},{j})",end="")
        print("|")
    print("======"*length + "=")     



def printBoardFull(board):
    print(f"""
-------------------------------------------Board Interface -----------------------------------------------
    
 ________________________________
|    EXPERIMENTAL VERSION:       |
|    Instruction: (x,y) with:    |
|          x = row               |
|          y = column            |
|________________________________|
    """)            
    IndexBoardInfo(blankboard)
    Board(blankboard)
    
    print("""
----------------------------------------------------------------------------------------------------------
    """)

def user_interface():
    while True:
        try:
            user_row = int(input(f"Enter a number for board's row: "))
            user_column = int(input(f"Enter a number for board's column: "))
            if user_row in range(0,length):
                if user_column in range(0,length):
                    if blankboard[user_row][user_column] == ' ':
                        blankboard[user_row][user_column] = player
                        break
                    else:
                        print("The box already filled, Please provide another answer")
                else:
                    print(f"Please enter a number from 0-{length}.")
            else:
                print(f"Please enter again!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    blankboard[user_row][user_column] = player

def win_condition(board):
    # Check rows
    for i in range(length):
        for j in range(length - 2):
            if board[i][j] == board[i][j+1] == board[i][j+2] == player:
                return True

    # Check columns
    for j in range(length):
        for i in range(length - 2):
            if board[i][j] == board[i+1][j] == board[i+2][j] == player:
                return True

    # Check diagonals
    for i in range(length - 2):
        for j in range(length - 2):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == player:
                return True

    for i in range(2, length):
        for j in range(length - 2):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == player:
                return True

    return False




def main():
    count = 0
    for i in range(length*length):
        count = count + 1

        print(f"\n Turn{count}")
        printBoardFull(blankboard)
        user_interface()

        if win_condition(blankboard) == True:
            printBoardFull(blankboard)
            print("We have a winner! ")
            break
        else:
            if count == length*length:
                printBoardFull(blankboard)
                print("Draw!!")
                
        switchPlayer()

if __name__ == "__main__":
    main()