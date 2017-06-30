# using this site: http://www.practicepython.org

# Function that checks for a winner
def check_winner(board):
    # board = [
    #     [x, 0, 0],
    #     [x, o, o],
    #     [x, 0, o] ]

    # We check for horizontal and vertical matches.
    for index in range(len(board)):
        if (str(board[index][0]) == "x" and str(board[index][1]) == "x" and str(board[index][2]) == "x") or (str(board[0][index]) == "x" and str(board[1][index]) == "x" and str(board[2][index]) == "x"):
            return "Player 1 wins!"
        elif (str(board[index][0]) == "o" and str(board[index][1]) == "o" and str(board[index][2]) == "o") or (str(board[0][index]) == "o" and str(board[1][index]) == "o" and str(board[2][index]) == "o"):
            return "Player 2 wins!"

    # we now check for diagonals
    count = 0
    for index in range(len(board)):
        if str(board[index][index]) == "x":
            count += 1
        else:
            break
    if count == 3:
        return "Player 1 wins!"

    count = 0
    for index in range(len(board)):
        if str(board[index][index]) == "o":
            count += 1
        else:
            break
    if count == 3:
        return "Player 2 wins!"

    # Check if the game is still going
    if any(0 in sublist for sublist in board):
        return ""
    return "Draw!"

def tick_tack_toe_game():
    player1_win = 0
    player2_win = 0
    draws = 0
    print("Welcome to Tick Tack Toe: Python Edition!")

    while True:
        board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        player_2_turn = False
        help_text = "P1, enter a coordinate to place your 'x'. Ex: 1,2: "

        while True:
            print_board(board)
            # Gets the user input to place their token down.
            user = raw_input(help_text).strip().split(",")
            row = int(user[0])
            col = int(user[1])
            if board[row][col] is 0:
                if player_2_turn == False:
                    board[row][col] = "x"
                    player_2_turn = True
                    help_text = "P1, enter a coordinate to place your 'x'. Ex: 1,2: "
                else:
                    board[row][col] = "o"
                    player_2_turn = False
                    help_text = "P2, enter a coordinate to place your 'o'. Ex: 1,2: "
            else:
                print("You dummy, you can't do that!")

            # Checks if there's a winner.
            result = check_winner(board)
            if result:
                print result
                if "2" in result:
                    player2_win += 1
                elif "1" in result:
                    player1_win += 1
                else:
                    draws += 1
                break

        # Prints out tallies and asks user if they want to play again
        print("P1 Wins: " + str(player1_win) + "\nP2 Wins: " + str(player2_win) + "\nDraws: " + str(draws))
        user = raw_input("Play again? yes or no: ").lower()
        if "yes" not in user:
            print("See Ya!")
            break
        else:
            print("Resetting game...")

# Helper functions
# This syntax simply means that you print out the specified string X times all on the same line
def print_horiz_times(times):
    print(" ---" * times)

def print_verti_times(times):
    print("|\t" * (times + 1))

def print_board(board):
    count = 0
    for x in range(len(board)):
        print_horiz_times(len(board))
        print("| " + str(board[count][0]) + " | " + str(board[count][1]) + " | " + str(board[count][2]) + " |")
        count += 1
    print_horiz_times(len(board))

# main execution
# By using the build in __name__, we can allow for a way to tell Python to go into this and act it as a main method...
if __name__ == "__main__":
    tick_tack_toe_game()
