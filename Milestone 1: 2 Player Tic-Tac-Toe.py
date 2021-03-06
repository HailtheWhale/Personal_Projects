from IPython.display import clear_output

# Initilizing Dictionary 
# Contains ALL the important game data.
# Repeatedly pulled and updated in used functions.
game_data = {"Desired_Position":0,"Next_Player": 1,"Game_Board":" ", "Player_1":"X", "Player_2":"O","Round":1, "Playing?":"Y","Game_Over?":False, "reset":True}

# Gameboard Data Function
# Based on indexing. Displays the current gameboard that is built
# from indexed strings pulled from a list. 
def tic_tac_board(game_data):
    board = game_data["Game_Board"]
    print("\nCurrent Game Board\n")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print("---------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("---------")
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("\n")
    
# Keypad Display 
# Simple Display to give players a visual aid where marks will go.
def keypad():
    print("Board position numbers are like a keypad:")
    print("[7]","[8]","[9]")
    print("[4]","[5]","[6]")
    print("[1]","[2]","[3]")
    print("\n")

# Player Choosing Function. 
# Set's X or O to whatever Player 1 chooses
# and sets Player 2 to the other one. 
def player_choosing(game_data):
    
    # Initializing
    player_chosen = False
    choice = " "
    
    # Loops until desired input achieved
    while player_chosen == False:
        choice = input("Player 1 Select X or O \n")
        
        # Variety of correct options 
        if choice in ["X","x","O","o"]:
            
            # .upper makes sure that it's capitalized 
            if choice.upper() == "X":
                game_data["Player_1"] = "X"
                game_data["Player_2"] = "O"
            else:
                game_data["Player_1"] = "O"
                game_data["Player_2"] = "X"
            
            # Displays what players are.
            print(f'\nPlayer 1 will be "{game_data["Player_1"]}"')
            print(f'Player 2 will be "{game_data["Player_2"]}"')
            
            # Breaks loop
            player_chosen = True 
            
        # Displays an error message 
        else: 
            print("That is not an Option.\n")
    
    # Updates Dictionary 
    return game_data

# User input Function. 
# Takes the desired position for a mark on the 
# Gameboard. Pulls Dictionary.
def user_input(game_data):
    
    # Initializing
    correct_input = False
    player_input = " "
    
    # Displaying who's turn it is
    print(f'Player {game_data["Next_Player"]}')
    
    # Loops until desired input is achieved 
    while correct_input == False:
        player_input = input("Select a Keypad Digit: ")
        
        # Error message if input is a # instead of a string
        if player_input.isdigit() == False:
            print("That is not a valid digit")
                  
        # If message is a number
        if player_input.isdigit() == True:
            # First checks if the spot on the board is taken. Displays error message 
            if game_data["Game_Board"][int(player_input)-1] in ["X","O"]:
                print("That spot is already taken.")
                  
            # Then checks if the given number is one on the previously displayed 
            # keypad based input range. 
            elif int(player_input) in range(1,10):
                  
                # Just to alternate between 1 and 2 for display data. 
                game_data["Next_Player"]=game_data["Next_Player"]+1
                  
                # If EVEN = Even Turn = Player 2 turn.
                if game_data["Next_Player"]%2 == 0:
                    game_data["Next_Player"]=2
                  
                # If ODD = Odd Turn = Player 1 Turn 
                else:
                    game_data["Next_Player"]=1
                    
                # Updates the indicated position on the board,
                # which will be called to place an X or O at the spot
                game_data["Desired_Position"]=int(player_input)
                  
                # Breaks loop
                correct_input = True
                
            # Displays an Error Message 
            else:
                print("That is not a digit on the keypad")
    
    # Updates Dictionary
    return game_data

# Updating Gameboard Function.
# Replaces the desired postion on the gameboard based on 
# who's turn it is and what their type of mark is
def board_update(game_data):
                  
    # List indexing starts from 0, not 1. Accounts for that.
    player_input = game_data["Desired_Position"]-1
                  
    # A bunch of checks to make sure that the right mark is being placed 
    # in the indicated spot.
    if game_data["Next_Player"] == 2 and game_data['Player_1'] == "X":
        game_data["Game_Board"][player_input] = "X"
    if game_data["Next_Player"] == 2 and game_data['Player_1'] == "O":
        game_data["Game_Board"][player_input] = "O"
    if game_data["Next_Player"] == 1 and game_data['Player_2'] == "X":
        game_data["Game_Board"][player_input] = "X"
    if game_data["Next_Player"] == 1 and game_data['Player_2'] == "O":
        game_data["Game_Board"][player_input] = "O"

# Continue Playing Function
def continue_playing(game_data):
                  
    # Initializing 
    question = True 
    
    
    # Loops until desired input is achieved.
    while question == True:
        user_input = input("\nAre You Still Playing (Y or N)? ")
        
        # If input is what's needed
        if user_input in ["Y","N"]:
                  
            # Breaks loop. Updates game data.
            question = False
            game_data["Playing?"] = user_input
        
        # Displays Error message. 
        else:
            print("That's not an Option.")
    
    # Updates Dictionary 
    return game_data 
    
# Win Check Function 
# Many checks to make sure the board is still playable
# and someone has not won yet. Calls 2 simple functions 
# To reduce the already bulky checks. 
def game_over(game_data):
    
    # To reduce complexity of Game Board Checks 
    board = game_data["Game_Board"]
    
    # If the game's playable
       if " " in board:
        # All checking if there's 3 in a row. Pulls 3 simple functions
        # To deal with repeated conditional updates. 
        if board[0:3] == ["X","X","X"]:
            update(game_data)
            x_wins()
        if board[0:3] == ["O","O","O"]:
            update(game_data)
            o_wins()
        if board[3:6] == ["X","X","X"]: 
            update(game_data)
            x_wins()
        if board[3:6] == ["O","O","O"]:
            update(game_data)
            o_wins()
        if board[6:] == ["X","X","X"] or board[6:] == ["O","O","O"]:
            update(game_data)
        if board[0] == board[3] == board[6] == "X":
            update(game_data)
            x_wins()
        if board[0] == board[3] == board[6] == "O":
            update(game_data)
            o_wins()
        if board[1] == board[4] == board[7] == "X":
            update(game_data)
            x_wins()
        if board[1] == board[4] == board[7] == "O":
            update(game_data)
            o_wins()
        if board[2] == board[5] == board[8] == "X":
            update(game_data)
            x_wins()
        if board[2] == board[5] == board[8] == "O":
            update(game_data)
            o_wins()
        if board[0] == board[4] == board[8] == "X":
            update(game_data)
            x_wins()
        if board[0] == board[4] == board[8] == "O":
            update(game_data)
            o_wins()
        if board[2] == board[4] == board[6] == "X":
            update(game_data)
            x_wins()
        if board[2] == board[4] == board[6] == "O":
            update(game_data)
            o_wins()
            
    # Else, the game's not playable. It's a tie. 
    else:
        print("Tie!")
        update(game_data)
            
    # Updates Dictionary 
    return game_data 

# Updates Dictionary. Just to reduce typing. 
def update(game_data):
    print("Game Over!")
    game_data["Game_Over?"] = True
    return game_data

# Displays X Winner. Just to Reduce Typing 
def x_wins():
    if game_data["Player_1"] == "X":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

# Displays O Winner. Just to Reduce Typing 
def o_wins():
    if game_data["Player_1"] == "O":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

# Same as Continue Playing Function 
# Just put here to help organize. NO Dictionary updates 
def play_again():
    # Initializing 
    question = True 
    response = " "
    
    while question == True:
        user_input = input("Continue Playing (Y or N)? ")
        if user_input in ["Y","N"]:
            question = False
            response = user_input
        else:
            print("That's not an Option.")
            
    return response

#############################################################

# MAIN Code
while game_data["reset"] == True:
    
    # Resetting All Variables 
    game_data["reset"] = False
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_data["Game_Board"] = board
    game_data["Round"] = 1
    game_data["Game_Over?"] = False
    game_data["Playing?"] = "Y"
    
    # Assigning marks to players 
    player_choosing(game_data)
    
    continue_playing(game_data)

    # Loops until Players want to quit  
    while game_data["Playing?"] == "Y":
        # Clears previous Display 
        clear_output()
        
        # Displays game board position indeces 
        keypad()
                  
        # Loads the board 
        tic_tac_board(game_data)
                  
        # Displays the round 
        print("Round " + str(game_data["Round"]) + "\n")
    
        # Loops twice so that both players can go 
        for num in range (1,3):
            
            # Gets user input 
            user_input(game_data)
                  
            # Places the mark at the inputted spot 
            board_update(game_data)
                  
            # Displays updated board 
            tic_tac_board(game_data)
            
            # Checks if game is over via 3 in a row or tied. 
            game_over(game_data)
                  
            # If the game's over, ask if still playing.
            if game_data["Game_Over?"] == True:
                continue_playing(game_data)
                break
            
        # If game's over
        if game_data["Game_Over?"] == True: 
                  
            # If not playing, break out of the loop and the code ends 
            if game_data["Playing?"] == "N":
                break
                  
            # If still playing, clears screen and makes the outermost 
            # loop now true so the game runs again. 
            elif game_data["Playing?"] == "Y":
                clear_output()
                print("Resetting...")
                game_data["reset"] = True
                break
        # If game's not over 
        elif game_data["Game_Over?"] == False:
                continue_playing(game_data)
        
        # Updates the Round
        game_data["Round"] = game_data["Round"]+1
