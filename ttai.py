# Griffin Withington's Tic-Tac-Toe Game
# Playing vs. AI

#Skeleton Code First
import random


# Create Structure for board that can be updated
# Print board with each new turn

# Enter in winning data requirement
def new_board():
    return [[None,None,None],[None,None,None],[None,None,None]]
    
    
    


board = new_board()

board[2][2] = "X"
board[0][1] = "X"
board[1][0] = "X"
board[1][2] = "O"
board[0][2] = "O"
board[2][0] = "O"



# RENDER FUNCTION PRINTS CURRENT BOARD STATE
def render(board):
    rend = [[],[],[]]
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == None:
                rend[row].append(" ")
            else:
                rend[row].append(board[row][column])
    print("  0 1 2")
    print("  -----")
    print("0|" + rend[0][0] + " " + rend[0][1] + " " + rend[0][2])
    print("1|" + rend[1][0] + " " + rend[1][1] + " " + rend[1][2])
    print("2|" + rend[2][0] + " " + rend[2][1] + " " + rend[2][2])
    print("  -----")








#This is a GET_MOVE function that returns the coordinates of a move as 
# a tuple of the x & y coordinates of their move
def get_move():
    row = int(input("Choose row (0-2): "))  
    while row not in [0, 1, 2]:
        row = int(input("*Choice Invalid* Choose valid row from 0 to 2: "))  
    column = int(input("Choose column (0-2): ")) 
    while column not in [0, 1, 2]:
        column = int(input("*Choice Invalid* Choose valid column from 0 to 2: "))
    return(int(row), int(column))
    
    








# This is a MAKE_MOVE function that takes the get_move tuple and 
# inplements it onto the board
def make_move(old_board, tup, player):
    new_board = [[],[],[]]
    for row in range(0,3):
        for column in range(0,3):
            new_board[row].append(board[row][column])
    new_board[tup[0]][tup[1]] = player 
    return new_board






# Determining a winner!
def get_winner(board):
    lines = [
    # Hotizontals
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],
    # Verticals
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    # Diagonals
    [board[0][0], board[1][1], board[2][2]],
    [board[0][2], board[1][1], board[2][0]]
    ]


    for line in lines:
        if line == ["X","X","X"]:  
            return "X"
        elif line == ["O","O","O"]:
            return "O"




#############################################################

#     AI TIME   #

#############################################################




def ai(player, board):
    tup = (1, 2) # coordinates of AI's move
    return tup



def randomai(player, board):
    x = random.randint(0,2)
    y = random.randint(0,2)
    while board[x][y] != None:
        x = random.randint(0,2)
        y = random.randint(0,2)
    tup = (x, y)
    return tup
"""
####
# AI RANDOM TEST
ai_move = randomai("O", board)    
            
make_move(board, ai_move, "O")

render(board)
####

"""


def finds_winning_moves_ai(player, board):
    lines = [
    # Hotizontals
    [board[0][0], board[0][1], board[0][2],0,0,0,1,0,2],
    [board[1][0], board[1][1], board[1][2],1,0,1,1,1,2],
    [board[2][0], board[2][1], board[2][2],2,0,2,1,2,2],
    # Verticals
    [board[0][0], board[1][0], board[2][0],0,0,1,0,2,0],
    [board[0][1], board[1][1], board[2][1],0,1,1,1,2,1],
    [board[0][2], board[1][2], board[2][2],0,2,1,2,2,2],
    # Diagonals
    [board[0][0], board[1][1], board[2][2],0,0,1,1,2,2],
    [board[0][2], board[1][1], board[2][0],0,2,1,1,2,0]
    ]
    tup = (3, 3)
    for line in lines:
        if line[0:3] == [player, player, None]:
            tup = (line[7], line[8])
        elif line[0:3] == [player, None, player]:
            tup = (line[5], line[6])
        elif line[0:3] == [None, player, player]:
            tup = (line[3], line[4])
    if tup == (3, 3):
        tup = randomai(player, board)        
    return tup        

           




def find_block_ai(player, board):
    if player == "X":
        opp = "O"
    if player == "O":
        opp = "X"
    lines = [
    # Hotizontals
    [board[0][0], board[0][1], board[0][2],0,0,0,1,0,2],
    [board[1][0], board[1][1], board[1][2],1,0,1,1,1,2],
    [board[2][0], board[2][1], board[2][2],2,0,2,1,2,2],
    # Verticals
    [board[0][0], board[1][0], board[2][0],0,0,1,0,2,0],
    [board[0][1], board[1][1], board[2][1],0,1,1,1,2,1],
    [board[0][2], board[1][2], board[2][2],0,2,1,2,2,2],
    # Diagonals
    [board[0][0], board[1][1], board[2][2],0,0,1,1,2,2],
    [board[0][2], board[1][1], board[2][0],0,2,1,1,2,0]
    ]
    tup = (3, 3)
    for line in lines:
        if line[0:3] == [player, player, None]:
            tup = (line[7], line[8])
        elif line[0:3] == [player, None, player]:
            tup = (line[5], line[6])
        elif line[0:3] == [None, player, player]:
            tup = (line[3], line[4])
        elif line[0:3] == [opp, opp, None]:
            tup = (line[7], line[8])
        elif line[0:3] == [opp, None, opp]:
            tup = (line[5], line[6])
        elif line[0:3] == [None, opp, opp]:
            tup = (line[3], line[4])
    if tup == (3, 3):
        tup = randomai(player, board)        
    return tup 


"""

####
# AI RANDOM FIND WIN TEST
render(board)

ai_move = randomai("O", board)    
            
make_move(board, ai_move, "O")

render(board)

ai_win_move = finds_winning_moves_ai("O", board)

make_move(board, ai_win_move, "O")

render(board)
####

"""





#  PERFECT AI



def legal_moves(board):
    moves = []
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == None:
                moves.append((row, column)) 
    return moves
    
    
    
    
#########
# TESTING GROUND

"""
render(board)

new_board = make_move(board, (0,0), "X")

render(new_board)
render(board)


"""
##########3







def minimax_score(board):
    
    if len(legal_moves(board)) % 2 == 0:
        player = "O"
    else:
        player = "X"
   
                     
        
    if get_winner(board) == "X":
        return 10
    elif get_winner(board) == "O":
        return -10
    elif len(legal_moves(board)) == 0: 
        return 0
    
    
    score = []
    
    for move in legal_moves(board):
        new_board = make_move(board, move, player)
        score.append(minimax_score(new_board))
    
    
    
    if player == "X":
        return max(score)
    if player == "O":
        return min(score)
    
    
    
   



##################
# TESTING GROUND


render(board)


print("Minimax score: " + str(minimax_score(board)))






#############################################################

#     AI DONE   #

#############################################################









def main():
    print()
    print()
    print("Welcome to Tic-Tac-Toe!")
    print()
    print()
    
    
    board = new_board()
    render(board)
    human = input("Choose to play as X or O: ")
    while human not in ["X", "O"]:
        print("*INVALID* Choose either X or O (use caps)")
        human = input("Selection: ")
    for turn in range(0, 9):
        
        #Assigning Player Turn
        if turn % 2 == 0:
            player = "X"
        else:
            player = "O"
            
        print("It's " + player + "'s Turn!")
        
        
        # Getting move from player
        
        if player == human:
            move_coords = get_move()
            while board[move_coords[0]][move_coords[1]] != None:
                print("*SPACE OCCUPIED*")
                print("Please choose again")
                move_coords = get_move()
        else:    
            move_coords = find_block_ai(player, board)
            
        # Implementing move from player
        board = make_move(board, move_coords, player)

        render(board)
        
        
        
     #########################   
        if get_winner(board) == "end":
            return   
      #######################      
    
    print("Shucks! A Draw!")
    return




"""
# Loop through turns until the game ends
loop forever:
    # TODO
    current_player = ???
 
# Print current state of the board   
render(board)

# Get the move that the current player is gonna make
move_co_ords = get_move()

# Make the move that we calculated above
make_move(board, move_co_ords, current_player)

# Work out if there's a winner
winner = get_winner(board)

# If there is a winner, crown them the champion
# and exit the loop
if winner is not None:
    print "WINNER IS " + str(winner) + "!"
    
# If there is not winner and the board is full, exit loop
if is_board_full(board):
    print "Draw..."
    
# Repeat until game is over


""" 
"""

if __name__ == "__main__":
    main()
    
"""    
  
    
    
    
    
    

