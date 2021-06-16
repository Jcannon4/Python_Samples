import sys, os
while(1 == 1):
#displays board, board is a list.
    def display_board(board):
        print(board[0]+"|"+board[1]+'|'+board[2])
        print('-|-|-')
        print(board[3]+'|'+board[4]+'|'+board[5])
        print('-|-|-')
        print(board[6]+'|'+board[7]+'|'+board[8])    

#number is 1-9 user input. that spot in the list is changed to X
    def markerX(number, board):
        board[number] = 'X'
    
#number is 1-9 user input. that spot in the list is changed to 0
    def markerY(number, board):
        board[number] = 'O'

#returns boolean, checks to see if that spot on the board is open
    def check_position(number, board):
        if(board[number] == 'X' or board[number] == 'O'):
            return False
        else:
            return True

    def winner(board):
        if(board[0] == 'X' and board[1] == 'X' and board[2] == 'X'):
            return True
        elif(board[0] == 'X' and board[3] == "X" and board[6] == 'X'):
            return True
        elif(board[0] == 'X' and board[4] == "X" and board[8] == 'X'):
            return True
        elif(board[1] == 'X' and board[4] == "X" and board[7] == 'X'):
            return True
        elif(board[2] == 'X' and board[5] == "X" and board[8] == 'X'):
            return True
        elif(board[2] == 'X' and board[4] == "X" and board[6] == 'X'):
            return True
        elif(board[3] == 'X' and board[4] == "X" and board[5] == 'X'):
            return True
        elif(board[6] == 'X' and board[7] == "X" and board[8] == 'X'):
            return True
        elif(board[0] == 'O' and board[1] == 'O' and board[2] == 'O'):
            return True
        elif(board[0] == 'O' and board[3] == "O" and board[6] == 'O'):
            return True
        elif(board[0] == 'O' and board[4] == "O" and board[8] == 'O'):
            return True
        elif(board[1] == 'O' and board[4] == "O" and board[7] == 'O'):
            return True
        elif(board[2] == 'O' and board[5] == "O" and board[8] == 'O'):
            return True
        elif(board[2] == 'O' and board[4] == "O" and board[6] == 'O'):
            return True
        elif(board[3] == 'O' and board[4] == "O" and board[5] == 'O'):
            return True
        elif(board[6] == 'O' and board[7] == "O" and board[8] == 'O'):
            return True
        else:
            return False
    def cats_game(player, turn):
        if(player == 'O' and turn == 10):
            return True
        elif(player == 'X' and turn == 9):
            return True
        else:
            return False
    def play_again(replay):
        if(replay == 'Y' or replay == 'y'):
            print('OK')
        else:
            print('Thanks for playing!')
            sys.exit()
    turn = 0
    player1 = input('Please select X or O\n')
    player2 = ''

#Input is player1, other option is player 2
    if (player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
        turn = turn + 1 #starts player at markerY
    print('player1 is ' + player1)
    print('player2 is ' + player2)

#shows player the input board so number choices make sense, shown once
    input_board = ['1','2','3','4','5','6','7','8','9']
    display_board(input_board)

#the actual game board list, empty at beginning.
    game_board  = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

#while loop that runs game, stops when a winning combo is found
    while(winner(game_board) == False and cats_game(player1, turn) == False):
        if(turn%2 == 0):
            turn = turn +1
            position = int(input('Please enter in a number 1-9\n')) -1
            if(check_position(position, game_board)):
                markerX(position,game_board)
                display_board(game_board)
                print('\n')
            else:
                turn = turn - 1
                print('That spot is taken! Select another spot...')
                display_board(game_board)
        
            continue

        else:
            turn = turn + 1
            positiony = int(input('Please enter a number 1-9\n')) -1
            if(check_position(positiony, game_board)):
                markerY(positiony, game_board)
                display_board(game_board)
                print('\n')    
            else:
                turn = turn -1
                print('That spot is taken! Select another spot...')
                display_board(game_board)
            continue
    if(winner(game_board)):
        if(turn%2 == 1 and player1 == 'X'):
            print(player1 + " is the winner!")
        elif(turn%2 == 0 and player1 == 'X'):
            print(player2 + " is the winner!")
        elif(turn%2 == 0 and player1 == 'O'):
            print(player1 + " is the winner!")
        elif(turn%2 == 1 and player1 == 'O'):
            print(player2 + " is the winner!")
    if(cats_game(player1, turn) and winner(game_board) == False):
        print('Cats game! Its a tie!')

    replay =input("Would you like to play again?(Y/N)\n")
    play_again(replay)

    continue
