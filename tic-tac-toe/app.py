
#tictactoe

#board for game using key and value pair
board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}

#displaying layout of the board
def displayBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")

displayBoard(board)

#checking vacant position 
def vacantSpace(position):
  if(board[position]== ' '):
    return True
  else:
    return False

#checking for draw event
def checkDraw():
  for key in board.keys():
      if board[key] == ' ':
          return False
          
  return True

#checking for win event
def checkWin():
  if(board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
    return True
  elif(board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
    return True
  elif(board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
    return True
  elif(board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
    return True
  elif(board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
    return True
  elif(board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
    return True
  elif(board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
    return True
  elif(board[3] == board[5] and board[3] == board[7] and board[3] != ' '):
    return True
  else:
    return False

#check who won (X or O)
def checkWhichMarkWon(mark):
  if(board[1] == board[2] and board[1] == board[3] and board[1] !=mark):
    return True
  elif(board[4] == board[5] and board[4] == board[6] and board[4] !=mark):
    return True
  elif(board[7] == board[8] and board[7] == board[9] and board[7] !=mark):
    return True
  elif(board[1] == board[4] and board[1] == board[7] and board[1] !=mark):
    return True
  elif(board[2] == board[5] and board[2] == board[8] and board[2] !=mark):
    return True
  elif(board[3] == board[6] and board[3] == board[9] and board[3] !=mark):
    return True
  elif(board[1] == board[5] and board[1] == board[9] and board[1] !=mark):
    return True
  elif(board[3] == board[5] and board[3] == board[7] and board[3] !=mark):
    return True
  else:
    return False


#insert symbol
def insertSymbol(symbol,position):
    if vacantSpace(position):
        board[position] = symbol
        displayBoard(board)
        
        if checkWin():
            if symbol == 'X':
              print("Computer Wins!")
              exit()
            
            else:
                print("Player wins")
                exit()
        
        if(checkDraw()):
          print("Game Draw!")
          exit()

    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertSymbol(symbol,position)
        return

#initializing symbol
playerSymbol = 'O'
computerSymbol = 'X'


def playerMove():
  position = int(input("Enter the position for 'O':"))
  insertSymbol(playerSymbol,position)
  return

def computerMove():
    bestScore = -800
    bestMove = 0

    for key in board.keys():
        if(board[key]==' '):
           board[key] = computerSymbol #maximizing moment
           score = minimax(board,0,False) #minimizing moment
           board[key] = ' ' #to play again the next move

           if(score > bestScore):
              bestScore = score
              bestMove = key
    
    insertSymbol(computerSymbol,bestMove)
    return

#minimax algorithm implementation
def minimax(board,depth,isMaximizing):
    if checkWhichMarkWon(computerSymbol):
      return 1
    elif checkWhichMarkWon(playerSymbol):
      return -1
    elif checkDraw():
      return 0

    if isMaximizing:      #playing as a computer
      bestScore = -800
      for key in board.keys():
        if(board[key]==' '):
           board[key] = computerSymbol
           score = minimax(board,0,False) 
           board[key] = ' ' 

           if(score > bestScore):
              bestScore = score
      
      return bestScore

    else: #it is executed first
      bestScore = 800       #enemy bot
      for key in board.keys():
        if(board[key]==' '):
           board[key] = computerSymbol #minmizing
           score = minimax(board,0,True) #calling maximizing
           board[key] = ' ' #to play again the next move

           if(score < bestScore):
              bestScore = score

      return bestScore


print("Computer starts first.\n")
#condition for game run
while not checkWin():
    computerMove()
    playerMove()





