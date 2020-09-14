#! python3
# tic_tac_toe - Play Tic-Tac-Toe against the CPU

"""
Super Tic-Tac-Toe(TTT) rules - There is one large 9 square grid with each grid square containing a smaller TTT
board. The aim of the game is to win the larger grid by getting three in a row. You can win an individual square of the
large grid by winning the smaller TTT game inside it. Therefore you need to win at least three smaller games of TTT to
win the large game. Player 1 starts by choosing any of the smaller games and making a move (X or O). Player 2 then
makes their move but must play on the smaller game positioned in the larger game grid which corresponds to that of the
position Player 1 played in the first small game grid.

e.g. P1 plays X in the top-middle position of the game in the top left of the large game grid. P2 must then play on the
top-middle game of the large game grid, although they can play any space within that game. If a small game is won and
no more moves are possible in that small game, a player who has to play there for their move can choose to play in any
small game of their choosing.
"""

import copy
import random


def draw_board(board):
    print()
    print(board[7][7] + '|' + board[7][8] + '|' + board[7][9] + ' # '
          + board[8][7] + '|' + board[8][8] + '|' + board[8][9] + ' # '
          + board[9][7] + '|' + board[9][8] + '|' + board[9][9])
    print('-+-+-' + ' # ' + '-+-+-' + ' # ' + '-+-+-')
    print(board[7][4] + '|' + board[7][5] + '|' + board[7][6] + ' # '
          + board[8][4] + '|' + board[8][5] + '|' + board[8][6] + ' # '
          + board[9][4] + '|' + board[9][5] + '|' + board[9][6])
    print('-+-+-' + ' # ' + '-+-+-' + ' # ' + '-+-+-')
    print(board[7][1] + '|' + board[7][2] + '|' + board[7][3] + ' # '
          + board[8][1] + '|' + board[8][2] + '|' + board[8][3] + ' # '
          + board[9][1] + '|' + board[9][2] + '|' + board[9][3])
    print('#' * 21)

    print(board[4][7] + '|' + board[4][8] + '|' + board[4][9] + ' # '
          + board[5][7] + '|' + board[5][8] + '|' + board[5][9] + ' # '
          + board[6][7] + '|' + board[6][8] + '|' + board[6][9])
    print('-+-+-' + ' # ' + '-+-+-' + ' # ' + '-+-+-')
    print(board[4][4] + '|' + board[4][5] + '|' + board[4][6] + ' # '
          + board[5][4] + '|' + board[5][5] + '|' + board[5][6] + ' # '
          + board[6][4] + '|' + board[6][5] + '|' + board[6][6])
    print('-+-+-' + ' # ' + '-+-+-' + ' # ' + '-+-+-')
    print(board[4][1] + '|' + board[4][2] + '|' + board[4][3] + ' # '
          + board[5][1] + '|' + board[5][2] + '|' + board[5][3] + ' # '
          + board[6][1] + '|' + board[6][2] + '|' + board[6][3])
    print('#' * 21)
    print(board[1][7] + '|' + board[1][8] + '|' + board[1][9] + ' # '
          + board[2][7] + '|' + board[2][8] + '|' + board[2][9] + ' # '
          + board[3][7] + '|' + board[3][8] + '|' + board[3][9])
    print('-+-+-' + ' # ' + '-+-+-' + ' # ' + '-+-+-')
    print(board[1][4] + '|' + board[1][5] + '|' + board[1][6] + ' # '
          + board[2][4] + '|' + board[2][5] + '|' + board[2][6] + ' # '
          + board[3][4] + '|' + board[3][5] + '|' + board[3][6])
    print('-+-+-' + ' # ' + '-+-+-' + ' # ' + '-+-+-')
    print(board[1][1] + '|' + board[1][2] + '|' + board[1][3] + ' # '
          + board[2][1] + '|' + board[2][2] + '|' + board[2][3] + ' # '
          + board[3][1] + '|' + board[3][2] + '|' + board[3][3])
    print()
def input_player_letter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item and the
    # CPU's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # The first element in the list is the player's letter; the second the CPU's.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, letter, lb, sb):
    board[lb][sb] = letter

def make_move_small(board, letter, sb):
    board[sb] = letter


def is_winner_small(bo, lb, le):
    # Given a board and a player's letter, this function returns True if that
    # player has won.
    # bo = board lb = large board position
    return ((bo[lb][7] == le and bo[lb][8] == le and bo[lb][9] == le) or  # Across Top
            (bo[lb][4] == le and bo[lb][5] == le and bo[lb][6] == le) or  # Across Mid
            (bo[lb][1] == le and bo[lb][2] == le and bo[lb][3] == le) or  # Across Bot
            (bo[lb][7] == le and bo[lb][4] == le and bo[lb][1] == le) or  # Down Left
            (bo[lb][8] == le and bo[lb][5] == le and bo[lb][2] == le) or  # Down Middle
            (bo[lb][9] == le and bo[lb][6] == le and bo[lb][3] == le) or  # Down Right
            (bo[lb][7] == le and bo[lb][5] == le and bo[lb][3] == le) or  # Diag RL
            (bo[lb][9] == le and bo[lb][5] == le and bo[lb][1] == le))    # Diag LR


def is_winner_large(wd, le):
    # Will check to see if there are three in a row on the large grid and returns True
    # if that player has won.
    # lb = large_board grid represented as list 'large_won', le is player letter
    return ((wd[7] == le and wd[8] == le and wd[9] == le) or  # Across Top
            (wd[4] == le and wd[5] == le and wd[6] == le) or  # Across Mid
            (wd[1] == le and wd[2] == le and wd[3] == le) or  # Across Bot
            (wd[7] == le and wd[4] == le and wd[1] == le) or  # Down Left
            (wd[8] == le and wd[5] == le and wd[2] == le) or  # Down Middle
            (wd[9] == le and wd[6] == le and wd[3] == le) or  # Down Right
            (wd[7] == le and wd[5] == le and wd[3] == le) or  # Diag RL
            (wd[9] == le and wd[5] == le and wd[1] == le))    # Diag LR


def get_large_won_copy(large_won):
    # Make copy of large_won list and return it.
    large_won_copy = []
    for i in large_won:
        large_won_copy.append(i)
    return large_won_copy


def get_board_copy(board):
    # Make a copy of the board list and return it.
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy

def get_small_board_copy(board, lb):
    # Make a copy of the board list and return it.
    board_copy = []
    for i in board[lb]:
        board_copy.append(i)
    return board_copy

def is_space_free(board, lb, move):
    # Return True if the passed move is free on the passed board.
    return board[lb][move] == ' '

def is_space_free_small(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ' '

def get_player_move(board, previous_small, large_won):
    if previous_small in large_won:
        previous_small = 0
    # Let the player enter their move.
    lb = ' '
    sb = ' '
    # When not first turn, large must be previous small.
    # If no positions are possible in that small grid it defaults to 0 again for a free choice.
    if previous_small == 0:
        while lb not in '1 2 3 4 5 6 7 8 9'.split() or is_board_full(board, int(lb)):
            print('Free choice of small game board. (1-9)')
            lb = input()
    else:
        if not is_board_full(board, previous_small):
            lb = previous_small
        else:
            while lb not in '1 2 3 4 5 6 7 8 9'.split() or is_board_full(board, int(lb)):
                print('Free choice of an unfinished small game board!')
                lb = input()

    while sb not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(lb), int(sb)):
        print('Choose position on small game board: ' + str(lb) + ' (1-9)')
        sb = input()
    return int(lb), int(sb)


def choose_random_move_from_list(board, lb, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, lb, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter, previous_small, large_won):
    if previous_small in large_won:
        previous_small = 0
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is the algorithm for Super Tic-Tac-Toe AI:

    # Check to see if can win on large board with free turn (previous small = 0).
    if previous_small == 0:
        for lb in range(1, 10):
            if lb not in large_won:
                for sb in range(1, 10):
                    small_board_copy = get_small_board_copy(board, lb)
                    winner_dict_copy = copy.deepcopy(winner_dict)
                    if is_space_free_small(small_board_copy, sb):
                        make_move_small(small_board_copy, computer_letter, sb)
                        if is_winner_large(small_board_copy, computer_letter):
                            winner_dict_copy[lb] = (computer_letter)
                            if is_winner_large(winner_dict_copy, computer_letter):
                                return lb, sb

    # Will return win for a random small grid on free turn if possible
    if previous_small == 0:
        possible_wins = []
        for lb in range(1, 10):
            if lb not in large_won:
                for sb in range(1, 10):
                    small_board_copy = get_small_board_copy(board, lb)
                    if is_space_free_small(small_board_copy, sb):
                        make_move_small(small_board_copy, computer_letter, sb)
                        if is_winner_large(small_board_copy, computer_letter):
                            possible_wins.append((lb, sb))
        if len(possible_wins) != 0:
            lb, sb = random.choice(possible_wins)
            return lb, sb

    # Check if can win in forced small and go there. (Alternative code)
    # if previous_small != 0:
    #     lb = previous_small
    #     for i in range(1, 10):
    #         board_copy = get_board_copy(board)  # board_copy = copy.deepcopy(board) <--- This works
    #         if is_space_free(board_copy, lb, i):
    #             board_copy = get_board_copy(board_copy)
    #             board_copy[lb][i] = computer_letter
    #             if is_winner_small(board_copy, lb, computer_letter):
    #                 return lb, i

    # Check if can win in forced small and go there.
    if previous_small != 0:
        lb = previous_small
        for i in range(1, 10):
            small_board_copy = get_small_board_copy(board, lb)
            if is_space_free_small(small_board_copy, i):
                make_move_small(small_board_copy, computer_letter, i)
                if is_winner_large(small_board_copy, computer_letter):
                    return lb, i

    # Check if the player could win on their next move in small board and block them.
    if previous_small != 0:
        lb = previous_small
        for i in range(1, 10):
            small_board_copy = get_small_board_copy(board, lb)
            if is_space_free_small(small_board_copy, i):
                make_move_small(small_board_copy, player_letter, i)
                if is_winner_large(small_board_copy, player_letter):
                    return lb, i


    # Try to take one of the corners, if they are free, using previous_small.
    if previous_small != 0:
        lb = previous_small
        move = choose_random_move_from_list(board, lb, [1, 3, 7, 9])
        if move != None:
            return lb, move

        # Try to take the center, if it is free.
        if is_space_free(board, lb, 5):
            return lb, 5

        # Move on one of the sides.
        else:
            move = choose_random_move_from_list(board, lb, [2, 4, 6, 8])
            if move != None:
                return lb, move

    # If previous_small == 0 and no wins available choose random move.
    possible_moves = []
    for lb in range(1, 10):
        if lb not in large_won:
            for sb in range(1, 10):
                if is_space_free(board, lb, sb):
                    possible_moves.append((lb, sb))
    lb, sb = random.choice(possible_moves)
    return lb, sb


def is_board_full(board, lb):
    # Return True if every space on the board has been taken.
    # Otherwise, return False.
    for i in range(1, 10):
        if is_space_free(board, lb, i):
            return False
    return True

def is_large_full(large_won):
    for i in range(1, 10):
        if i not in large_won:
            return False
    return True


print('Welcome to Super Tic-Tac-Toe!')


while True:
    # Reset the board.
    the_board = [[' '] * 10, [' '] * 10, [' '] * 10, [' '] * 10, [' '] * 10,
                 [' '] * 10, [' '] * 10, [' '] * 10, [' '] * 10, [' '] * 10]

    large_won = []

    winner_dict = {1: None, 2: None, 3: None, 4: None, 5: None,
                   6: None, 7: None, 8: None, 9: None, 10: None}

    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    game_is_playing = True
    previous_small = 0


    while game_is_playing:
        if turn == 'player':
            draw_board(the_board)
            large, small = get_player_move(the_board, previous_small, large_won)
            previous_small = small
            make_move(the_board, player_letter, large, small)
            print('You played at: ' + str(large) + ' > ' + str(small))
            if is_winner_small(the_board, large, player_letter):
                for i in range(1, 10):
                    the_board[large][i] = player_letter
                large_won.append(large)
                winner_dict[large] = player_letter

            if is_winner_large(winner_dict, player_letter):
                print()
                print('$$$$$$$$$$$$$$$$$')
                print()
                draw_board(the_board)
                print('Hooray! You have won the game!')
                game_is_playing = False

            else:
                if is_large_full(large_won):
                    print('This board is full, it\'s a draw (1).')
                    game_is_playing = False
                else:
                    turn = 'computer'

        # Computer's turn
        else:
            large, small = get_computer_move(the_board, computer_letter, previous_small, large_won)
            previous_small = small
            make_move(the_board, computer_letter, large, small)
            print('The computer played: ' + str(large) + '>' + str(small))
            if is_winner_small(the_board, large, computer_letter):
                for i in range(1, 10):
                    the_board[large][i] = computer_letter
                large_won.append(large)
                winner_dict[large] = computer_letter

            if is_winner_large(winner_dict, computer_letter):
                draw_board(the_board)
                print('$£$£$£$£$£$£$£$£$£$£$£$£$£$£$£$')
                print()
                print('The computer has won. You suck!')
                print()
                game_is_playing = False

            else:
                if is_large_full(large_won):
                    draw_board(the_board)
                    print('This board is full, it\'s a draw (2).')
                    game_is_playing = False
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break

