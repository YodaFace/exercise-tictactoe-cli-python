import sys


#<--------- GLOBAL VARIABLES ---------># 

current_player = "X's"
next_player = "O's"
stop = False
board = [
    "-","-","-", 
    "-","-","-",    
    "-","-","-"
]

winner_is = ""

game_continues = True

#<--------- END GLOBAL VARIABLES ---------># 


def new_game():
    # your code here
    print("First player is " +current_player)
    display_board()
    play()

def display_board():
    print(f"""
    Current board ({current_player} turn):
    [{board[0]}] [{board[1]}] [{board[2]}]
    [{board[3]}] [{board[4]}] [{board[5]}]
    [{board[6]}] [{board[7]}] [{board[8]}]
    """)


def play():
    global current_player
    # your code here
    while game_continues == True:
        first_player()
        check_for_winner()
        second_player()
        check_for_winner()
    return
       
       
def first_player():
    print("Where do you want to place your mark?")
    position = input("Choose a position from 1-9: ")
    position = int(position) -1
    if position < 0:
        print("Value to low, please trye again.")
        position = input("Choose a position from 1-9: ")
    if position > 9:
        print("Value to high, please trye again.")
        position = input("Choose a position from 1-9: ")
    board[position] = "X"
    display_board()
    return
    # (ADD LATER) check_for_winner()
    # Moving on to second player
        
        
def second_player():     
    print("Current player is " +next_player)
    print("Where do you want to place your mark?")
    position = input("Choose a position from 1-9: ")
    position = int(position) -1
    if position < 0:
        print("Value to low, please trye again.")
        position = input("Choose a position from 1-9: ")
    if position > 9:
        print("Value to high, please trye again.")
        position = input("Choose a position from 1-9: ") 
    board[position] = "O"
    display_board()
    return
    ## FOR     StopIteration


def check_for_winner():
    # your code here
    global game_continues
    global winner_is
    check_if_win()
    if game_continues == True:
        print("No Winner")
    else: 
        print("The winner is "+winner_is)
        sys.exit()
    # check_if_tie(): 
    return


def check_if_win(): 
    global game_continues
    global winner_is
    #check_rows
    row_winner = check_rows()
    #check_columns
    column_winner = check_columns()
    #check_diagnals
    diaginal_winner = check_diagnals()

    # IS THERE A WINNER ?
    ## if game_continues == False:
    return    


def check_rows():
    global game_continues
    global winner_is
    # Check if any of the rows have all the same values
    # But not just the "-" being the same
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3 == True:
        game_continues = False

    # Return the winner
    if row_1:
        winner_is = board[2]
    elif row_2:
        winner_is = board[5]
    elif row_3:
        winner_is = board[8]
    return winner_is and game_continues



def check_columns():
    global game_continues
    global winner_is
    # Check if any of the rows have all the same values
    # But not just the "-" being the same
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3 == True:
        game_continues = False

    # Return the winner
    if column_1:
        winner_is = board[6]
    elif column_2:
        winner_is = board[7]
    elif column_3:
        winner_is = board[8]
    return winner_is and game_continues

def check_diagnals(): 
    global game_continues
    global winner_is
    # Check if any of the rows have all the same values
    # But not just the "-" being the same
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2 == True:
        game_continues = False

    # Return the winner
    if diag_1:
        winner_is = board[8]
    elif diag_2:
        winner_is = board[6]

    return winner_is and game_continues
    return


def check_if_tie(): 
    return


def change_player(): 
    return


new_game()



# while stop == False:
#     command = input("What do you want?: (start or stop)")
#     if command == "stop":
#         stop = True
#     # add commands here (if needed)
#     elif command == "start":
#         new_game()


# This was helpful : 
# https://www.youtube.com/watch?v=BHh654_7Cmw

