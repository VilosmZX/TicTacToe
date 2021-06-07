#!/usr/bin/python


# global variable
board = [
  "-","-","-",
  "-","-","-",
  "-","-","-"
]

game_still_going = True 

# winner 
winner = None 

# turn 
current_player = "X"

# Display Board
def screen():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])
  
def game():
  screen()
  while game_still_going:
    # Turn
    turn(current_player)
    # check if game over
    check_if_game_over()
    # flip player
    flip_player()
  
  # the game ended 
  if winner == "X" or winner == "O":
    print(winner + " won!")
  else:
    print("tie!")
    
    
def turn(player):
  
  print(player + "\'s turn")
  position = input("Choose a position from 1-9: ")
  
  valid = False
  while not valid:
    if position.isdigit() == False:
      position = input("Invalid input! Choose a position from 1-9: ")
  
    position = int(position) - 1 
  
    if board[position] != "-":
      valid = True
    elss:
      print("You cant go there. go again.")
  
  board[position] = player 
  
  screen()
  
def check_if_game_over():
  check_if_win()
  check_if_tie()
  
def check_if_win():
  global winner
  # check row
  row_winner = check_rows()
  colummn_winner = check_colummns()
  diagonal_winner = check_diagonals()
  
  if row_winner:
    winner = row_winner
  elif colummn_winner:
    winner = colummn_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None 
  # check collumn 
  # check diagonal
  return 

def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3: 
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif  row_3:
    return board[6]
  return

def check_colummns():
  global game_still_going
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"
  if col_1 or col_2 or col_3: 
    game_still_going = False
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif  col_3:
    return board[2]
  return

def check_diagonals():
  global game_still_going
  dia_1 = board[0] == board[4] == board[8] != "-"
  dia_2 = board[6] == board[4] == board[2] != "-"
  if dia_1 or dia_2: 
    game_still_going = False
  if dia_1:
    return board[0]
  elif dia_2:
    return board[6]
  return



def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    
  return
    
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  
  
  return
    

if __name__ == '__main__':
  game()
