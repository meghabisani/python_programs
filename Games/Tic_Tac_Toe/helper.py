from random import randint


# Clear the screen
def clear_output():
    print('\n'*100)


# Print the board
def display_board(board):
    clear_output()

    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('- | - | -')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- | - | -')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


# Takes a player input and assign their marker as 'X' or 'O'
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Assign the marker to the player's desired position
def place_marker(board, marker, position):
    board[position] = marker


# Checks to see if someone has won
def win_check(board, mark):
    i = 1
    # Horizontal lines check
    while i < 8:
        if board[i:i + 3] == [mark, mark, mark]:
            return True
        else:
            i += 3
            continue

    # Vertical lines check
    i = 1
    while i < 4:
        if board[i] == board[i + 3] == board[i + 6] == mark:
            return True
        else:
            i += 1
            continue

    # diagonal check
    if (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
        return True
    else:
        return False


# Randomly decide which player goes first
def choose_first():
    if randint(1, 2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# Returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '


# Checks if the board is full and returns a boolean value
def full_board_check(board):
    return ' ' not in board


# Asks for a player's next position
def player_choice(board):
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        try:
            pos = int(input('Choose your next position (1-9)'))
        except:
            print("I'm sorry, please try again.")

    return pos


# Asks the player if they want to play again and returns a boolean
def replay():
    ans = input('Do you want to play again (Y/N): ')
    return ans.upper() == 'Y'
