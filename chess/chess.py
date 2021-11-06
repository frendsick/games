#!/usr/bin/python3
from typing import List
from defs   import Board, Move, Player
from logic  import is_game_over
from move   import make_move
from utils  import print_board

def new_game():
    game_over: bool         = False
    whites_turn: bool       = True
    move_rule_counter: int  = 0 # 50 move rule

    players: List[Player] = [Player("White", "Teemu", 1337), Player("Black", "Random n00b", 420)]
    board = Board() # Initializes the board to the starting position
    moves: List[Move] = []
    # Game loop
    while not game_over:
        print_board(board, players)
        board = make_move(board, moves, players, whites_turn)
        game_over = is_game_over(board)
        whites_turn = not whites_turn

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