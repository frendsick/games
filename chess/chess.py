#!/usr/bin/python3
from defs   import Board
from logic  import is_game_over
from move   import ask_move, make_move
from utils  import print_board

def new_game():
    game_over: bool     = False
    whites_turn: bool   = True

    board = Board() # Initializes the board to the starting position

    # Game loop
    while not game_over:
        print_board(board)
        board = make_move(board, whites_turn)
        game_over = is_game_over(board)

def ask_play_again():
    while(True):
        print("Would you like to play again? (Y/n):")
        answer = input().upper()
        if answer == 'N':
            exit(0)
        elif answer == 'Y' or len(answer) == 0:
            main()
        else:
            print(f"Option '{answer}' is not recognized")

def main():
    new_game()
    ask_play_again()

if __name__ == '__main__':
    main()