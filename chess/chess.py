#!/usr/bin/python3
import pygame
from typing import List

from pygame import color
from defs   import Background, Board, Move, Player, BLACK, WHITE, SCREEN_HEIGHT, SCREEN_WIDTH
from logic  import is_game_over
from move   import make_move
from utils  import print_board, pygame_print_board
import itertools

def new_game():
    game_over: bool         = False
    whites_turn: bool       = True
    move_rule_counter: int  = 0 # 50 move rule
    players: List[Player] = [Player("White", "Teemu", 1337), Player("Black", "Random n00b", 420)]
    board = Board() # Initializes the board to the starting position
    moves: List[Move] = []

    colors = itertools.cycle((BLACK, WHITE))
    tile_size = SCREEN_WIDTH // 8
    width, height = 8*tile_size, 8*tile_size
    background = pygame.Surface((width, height))

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600,600))

    pygame_print_board(board, players, background, colors, tile_size)
    # Game loop
    while not game_over:
        clock.tick(30)
        screen.fill([60, 70, 90])
        screen.blit(background, (0, 0))

        print_board(board, players, game_over)
        move_rule_counter = make_move(move_rule_counter, board, moves, players, whites_turn)
        game_over = is_game_over(move_rule_counter, board, moves, players)
        whites_turn = not whites_turn
        pygame.display.update()
    print_board(board, players, game_over)

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
    pygame.init()
    new_game()
    ask_play_again()

if __name__ == '__main__':
    main()
