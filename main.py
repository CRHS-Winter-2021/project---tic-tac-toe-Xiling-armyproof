##Tic Tac Toe
#Name:Hao Tian
#Date:2/10/2021

#1. (Var) Setup the empty board as a list
theBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def print_ins():
  print ('Welcome to Tic Tac Toe game')
  print()
  print('the board looks like:\n')
  print('7' + '|' + '8' + '|' + '9')
  print("-----")
  print('4' + '|' + '5' + '|' + '6')
  print("-----")
  print('1' + '|' + '2' + '|' + '3')

  print('Follow the instructions in the game, \n')
  print('The program will tell you if your input is not correct \n')
  
  
  
  
  

def printBoard(theBoard):
    
      print(theBoard[7],'|',theBoard[8],'|',theBoard[9])
      print('----------')
      print(theBoard[4],'|',theBoard[5],'|',theBoard[6])
      print('----------')
      print(theBoard[1],'|',theBoard[2],'|',theBoard[3])

#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
    ask = input('player1 for X or O? \n')
    global player1
    global player2
    if ask == 'X' or ask =='x':
      player1 = 'X'
      player2 ='O'
      print('Now player1 is X, player2 is O')
    elif ask == 'O' or ask =='o':
      player1 = 'O'
      player2 ='X'
      print('Now player1 is O, player2 is X')

    else:
      print('input error, retry input')
      chooseLetter()
    

player = ''
player11 = ''
player22 = ''
#3b. (fun) Choose starting player 1 or 2
def chooseStart():
    global player22
    global player1
    global player2
    global player11
    ask = input('Who goes first (player1 or player2?) \n')
    if ask =='player1':
      player11 = player1
      player22 = player2
      print('player1 ({}) go first'.format(player1))
    elif ask =='player2':
      player22 = player1
      player11 = player2
      print('player2 ({}) go first'.format(player2))
    else:
      print('input error, retry input(player1/player2)')
      chooseStart()
      
    
   



#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(theboard, player):
  list1 = ['1','2','3','4','5','6','7','8','9']
  choice = (input('which position does {} goes\n'.format(player)))
  if choice in list1:
    choice = int(choice)
    if theBoard[choice] == ' ':
      theBoard[choice]= player

    elif theBoard[choice] != ' ':
      print('that position is occupied')
      playerMove(theboard, player)
  else:
    print('input error, retry input (range 1-9)')
    playerMove(theboard, player)

  




#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):
  if board[1] == board[2] == board[3] == player or board[4] == board[5] == board[6] == player or board[7] == board[8] == board[9] == player or board[1] == board[4] == board[7] == player or board[2] == board[5] == board[8] == player or board[3] == board[6] == board[9] == player or board[1] == board[5] == board[9] == player or board[3] == board[5] == board[7] == player:
    print('Player who use {}  win!!!!!!!'.format(player))
    print()
    False

  else:
    return True
  
    
    
  
  




#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    if board.count(' ')>1:
        return True

    elif board.count(' ')<=1:
        print('Board Full,DRAW')
        return False

def start():
  
  global theBoard
  answer = input('Do you want to play another game?\n')
  if answer == 'yes' or answer =='Yes' or answer =='YES':
    theBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    main()
  else:
    print('Game Over')

#7. Main function

def main():
    
    print_ins()
    #print instructions

    #game play
    #get player letter choice
    chooseLetter()
    print('______________________')  
    chooseStart()
    
    #checkFull(theBoard)
    print('______________________')  

    

    #while board is not full
    while True:
      
     ###first player move
        #player chooses move
      playerMove(theBoard, player11)
      print('______________________')  
        #print board
      printBoard(theBoard)
      print('______________________')
        #check win
      if not checkWin(theBoard, player11):
        break
        
         
        #check board full
      if not checkFull(theBoard):
        break
       
           
     
     ###first player move
        #player chooses move
      playerMove(theBoard, player22)
      print('______________________')  
        #print board
      printBoard(theBoard)
      print('______________________') 
        #check win
      if not checkWin(theBoard, player22):
        break
      
        
        #check board full
      if not checkFull(theBoard):
        break
      
    print('______________________')   
    
    #print('Game over byebye')

    start()
      
main()


