import os
import random


def clear():
    os.system('cls')


# Global variables
theBoard = [' '] * 10   # a list of empty spaces
moves = [str(num) for num in range(0, 10)]  # a List Comprehension


def display_board(a, b):
    print('TIC-TAC-TOE Board\n' + '  Available  ' + '  Playing\n  ' + 'Moves    ' + '    Board\n\n  ' +
          a[1]+'|'+a[2]+'|'+a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n  ' +
          '-----        -----\n  ' +
          a[4]+'|'+a[5]+'|'+a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6]+'\n  ' +
          '-----        -----\n  ' +
          a[7]+'|'+a[8]+'|'+a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9]+'\n')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1 : Choose X or O: ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker
    moves[position] = ' '


def win_check(board, mark):

    return ((board[7] == board[8] == board[9] == mark) or  # across the top
            (board[4] == board[5] == board[6] == mark) or  # across the middle
            (board[1] == board[2] == board[3] == mark) or  # across the bottom
            (board[7] == board[4] == board[1] == mark) or  # down the middle
            (board[8] == board[5] == board[2] == mark) or  # down the middle
            (board[9] == board[6] == board[3] == mark) or  # down the right side
            (board[7] == board[5] == board[3] == mark) or  # diagonal
            (board[9] == board[5] == board[1] == mark))  # diagonal


def random_player():
    return random.choice((-1, 1))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False  # Space is available on board
    return True  # Space is not available on board


def player_choice(board, player):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Player {}, choose your next position: (1-9) '.format(player)))
    return position


def replay():
    return input('Do you want to play again? Press "Y" to play: ').lower().startswith('y')


while True:
    clear()
    print('Welcome to Tic Tac Toe!')

    player1_marker, player2_marker = player_input()

    print('Player1 is: {}'.format(player1_marker))
    print('Player2 is: {}'.format(player2_marker))

    players = [0, player1_marker, player2_marker]
    toggle = random_player()
    player = players[toggle]

    print('For this round, Player {} will go first!'.format(player1_marker))

    play_game = input("Let's start the game.Press \"Y\" for Yes: ").lower()
    if play_game == 'y':
        game_on = True

        while game_on:
            display_board(moves, theBoard)
            position = player_choice(theBoard, player)
            place_marker(theBoard, player, position)

            if win_check(theBoard, player):
                display_board(moves, theBoard)
                print('Congratulations! Player ' + player + ' wins!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(moves, theBoard)
                    print('The game is a draw!')
                    break
                else:
                    toggle *= -1
                    player = players[toggle]
                    clear()

        # reset the board and available moves list
        theBoard = [' '] * 10
        moves = [str(num) for num in range(0, 10)]

        if not replay():
            break
    else:
        break
