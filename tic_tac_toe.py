#Tic Tac Toe Human vs Computer in python

import random

#Creating a list called board
board = [' ' for x in range(10)]
counter=0




#To insert the letter into the board
def insertLetter(letter, pos):
    board[pos] = letter

# To check space availability
def spaceIsFree(pos):
    return board[pos] == ' '


#The arrangement of tic tac toe during the game play
def printBoard(board):
    print('    |     |')
    print( board[1] +  '   | ' +  board[2] + '   | '  + board[3])
    print('    |     |')
    print('----------------')
    print('    |     |')
    print( board[4] +  '   | '  + board[5] + '   | ' + board[6])
    print('    |     |')
    print('----------------')
    print('    |     |')
    print( board[7] +  '   | ' + board[8] + '   | ' + board[9])
    print('    |     |')


#This function determine the winner based on the current board.
# Use bo instead of board and le instead of letter 
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #across the down
    (bo[4] == le and bo[5] == le and bo[6] == le) or #across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or #across the bottom
    (bo[1] == le and bo[4] == le and bo[7] == le) or #down the left side
    (bo[2] == le and bo[5] == le and bo[8] == le) or #down the middle
    (bo[3] == le and bo[6] == le and bo[9] == le) or #down the right side 
    (bo[1] == le and bo[5] == le and bo[9] == le) or #diagonal
    (bo[3] == le and bo[5] == le and bo[7] == le)) #diagonal

#Player input function with error-handling
def playerMove( ):
    run = True
    global counter
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                    
                #Space not free
                else:
                    print('Sorry, this space is occupied!')

            #Input out of range       
            else:
                print('Please type a number within the range!')

        #No number/not number enter
        except:
            print('Please type a number!')
    
    if move == int(move):
           counter +=1
           f =  open("logfile_21029137.txt", "a")
           f.write("\nTurn" + str({counter}))
           f.write("\nPlayer has placed x to position" + str({move}))
           f.close()

#Computer moves      
def compMove():
    possibleMove = [x for x,letter in enumerate(board) if letter==' ' and x!=0]
    move = 0

    # To check whether computer can win or not , if not then 
    # computer now tries to block opponent move, so that the player could not win
    for let in ['O','X']:
        for i in possibleMove:
            # replica of board 
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move
    
    if board[1] == 'X' or board[3]=='X' or board[7]=='X' or board[9]=='X':
        if 5 in possibleMove:
            move=5
            return move

    edgesOpen = []

    if (board[1] == 'X' and board[9]=='X') or (board[3]=='X' and board[7]=='X'):
            for i in possibleMove:
                if i in [2,4,6,8]:
                    edgesOpen.append(i)

    # randomly select a corner to move Into 
    if len(edgesOpen)>0:
        move = selectRandom(edgesOpen)
        return move

    # Same code repeat for edges also
    cornersOpen = []

    # Check whether there is any corner is empty if find empty then place
    # letter in that corner position

    for i in possibleMove:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    
    # randomly select a corner to move Into 
    if len(cornersOpen)>0:
        move = selectRandom(cornersOpen)
        return move


    # Place letter at center 
    if 5 in possibleMove:
        move = 5
        return move

    # Check whether there is any edge is empty if find empty then place
    # letter in that edge position

    for i in possibleMove:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    # randomly select a edge to move Into 
    if len(edgesOpen)>0:
        move = selectRandom(edgesOpen)
       
    return move

# randomly choose a position
def selectRandom(li):
    return random.choice(li)


#Check if the board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

   

#This function is called to start the game and dictate the flow of the program.
def main():
    #Main game loop
    print('Welcome to Tic Tac Toe!') 
    print('Each number represents the column below:')
    print('1|2|3')
    print('-----')
    print('4|5|6')
    print('-----')
    print('7|8|9')
    print('***************************')
    printBoard(board)
  

    #Check if the game has a winner or it's a tie game
    while not(isBoardFull(board)):
        
        #If the winner is computer
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\'s won!')
            break

        
        if not(isWinner(board, 'X')):
            move = compMove()

            #If no move for the computer means its a tie game
            if move == 0:
                print(' ')

            #The computer will place its move if got space    
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
                f =  open("logfile_21029137.txt", "a")
                f.write("\nComputer has placed O to position" + str({move}))
                f.close()
        #The player has won
        else:
            print('X\'s won! Good job')
            break

    #If the board is full, then it's tie game
    if isBoardFull(board):
        print('Tie Game!')
        
      
main()

# End game
while True:
    answer = input('Do you want to continue the game? Yes or No? (y/n)')

    #if player choose "y", the game will continue
    if answer.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()

    #If the player chooses "n", the function will break thus the program will end                          
    if answer.lower()== 'n':   
         print("Fair game,player. Farewell :)")
         break
        
    #If the player choose neither "y" or "n",
    else: 
     print("Choose either y or n only")
     answer

     
    
   

    








    






    




