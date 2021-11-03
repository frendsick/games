from defs   import Board
from logic  import is_game_over
from move   import ask_move, make_move
from utils  import print_board

def new_game():
    turn: int       = 1
    game_over: bool = False

    board = Board() # Initializes the board to the starting position

    # Game loop
    while not game_over:
        print_board(board)
        move = ask_move(turn)
        make_move(move, board, turn)
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