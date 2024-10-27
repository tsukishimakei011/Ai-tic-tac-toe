import random

# Creating a list called board
board = [' ' for x in range(10)]
counter = 0

# To insert the letter into the board
def insertLetter(letter, pos):
    board[pos] = letter

# To check space availability
def spaceIsFree(pos):
    return board[pos] == ' '

# The arrangement of tic-tac-toe during gameplay
def printBoard(board):
    print('    |     |')
    print(board[1] + '   | ' + board[2] + '   | ' + board[3])
    print('    |     |')
    print('----------------')
    print('    |     |')
    print(board[4] + '   | ' + board[5] + '   | ' + board[6])
    print('    |     |')
    print('----------------')
    print('    |     |')
    print(board[7] + '   | ' + board[8] + '   | ' + board[9])
    print('    |     |')

# This function determines the winner based on the current board
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[1] == le and bo[4] == le and bo[7] == le) or  # down the left side
            (bo[2] == le and bo[5] == le and bo[8] == le) or  # down the middle
            (bo[3] == le and bo[6] == le and bo[9] == le) or  # down the right side
            (bo[1] == le and bo[5] == le and bo[9] == le) or  # diagonal
            (bo[3] == le and bo[5] == le and bo[7] == le))    # diagonal

# Player input function with error handling
def playerMove():
    run = True
    global counter
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                    counter += 1
                    with open("logfile_21029137.txt", "a") as f:
                        f.write(f"\nTurn {counter}\nPlayer has placed X at position {move}")
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Minimax algorithm implementation
def minimax(new_board, depth, is_maximizing):
    if isWinner(new_board, 'O'):
        return 1
    elif isWinner(new_board, 'X'):
        return -1
    elif isBoardFull(new_board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(1, 10):
            if spaceIsFree(i):
                new_board[i] = 'O'
                score = minimax(new_board, depth + 1, False)
                new_board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(1, 10):
            if spaceIsFree(i):
                new_board[i] = 'X'
                score = minimax(new_board, depth + 1, True)
                new_board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Computer move using Minimax
def compMove():
    best_score = -float('inf')
    best_move = 0
    for i in range(1, 10):
        if spaceIsFree(i):
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    insertLetter('O', best_move)
    with open("logfile_21029137.txt", "a") as f:
        f.write(f"\nComputer has placed O at position {best_move}")
    return best_move

# Check if the board is full
def isBoardFull(board):
    return board.count(' ') == 1

# Main function to start the game and dictate the flow of the program
def main():
    print('Welcome to Tic Tac Toe!')
    print('Each number represents the position below:')
    print('1 | 2 | 3')
    print('---------')
    print('4 | 5 | 6')
    print('---------')
    print('7 | 8 | 9')
    print('***************************')
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print("O's won!")
            break

        if not isWinner(board, 'X'):
            move = compMove()
            print('Computer placed an O in position', move, ':')
            printBoard(board)
        else:
            print("X's won! Good job")
            break

    if isBoardFull(board):
        print('Tie Game!')

# Game continuation prompt
while True:
    main()
    answer = input('Do you want to play again? Yes or No? (y/n): ')
    if answer.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
    elif answer.lower() == 'n':
        print("Fair game, player. Farewell :)")
        break
    else:
        print("Please choose either y or n only.")






    




