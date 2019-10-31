from helper import *


# Game
def tic_tac_toe():

    print('Welcome to Tic Tac Toe!')
    while True:
        # Reset the board
        board = ['$'] + [' '] * 9
        mark1, mark2 = player_input()
        chance = choose_first()
        print(f'{chance} will go first')

        ans = input('Are you ready to play (Y/N): ').upper()

        if ans == 'N':
            game_on = False
        elif ans == 'Y':
            game_on = True
        else:
            print('Please answer correctly')
            continue

        while game_on:
            # Player 1 Turn
            if chance == 'Player 1':
                display_board(board)
                pos = player_choice(board)
                place_marker(board, mark1, pos)
                chance = 'Player 2'

                if win_check(board, mark1):
                    display_board(board)
                    print("\nCongratulations!! Player 1 has won!!\n")

                    game_on = False

            # Player2's turn.
            else:
                display_board(board)
                pos = player_choice(board)
                place_marker(board, mark2, pos)
                chance = 'Player 1'

                if win_check(board, mark2):
                    display_board(board)
                    print("\nCongratulations!! Player 2 has won!!\n")
                    game_on = False

            if full_board_check(board) and (not win_check(board, mark2)):
                display_board(board)
                print('\nThis game is draw\n')
                break

        if not replay():
            print('\nGoodBye!!')
            break


if __name__ == '__main__':
    tic_tac_toe()
