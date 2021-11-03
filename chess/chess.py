import re
from defs import Board

def new_game():
    board = Board

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