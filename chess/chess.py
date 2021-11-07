#!/usr/bin/python3
import itertools
import pygame
from typing import List
from defs   import Board, Move, Piece, Player, BLACK, WHITE, MOUSE_BUTTONS, TICKRATE, SCREEN_HEIGHT, SCREEN_WIDTH, Square
from logic  import is_game_over
from move   import make_move
from utils  import highlight_piece, print_board, print_board_background, print_board_state

def new_game():
    game_over: bool             = False
    highlighted_piece: Piece    = None
    whites_turn: bool           = True
    move_rule_counter: int      = 0 # 50 move rule
    players: List[Player]       = [Player("White", "Teemu", 1337), Player("Black", "Random n00b", 420)]
    board                       = Board() # Initializes the board to the starting position
    moves: List[Move]           = []

    # Pygame variables
    clock           = pygame.time.Clock()
    colors          = itertools.cycle((WHITE, BLACK))
    tile_height     = SCREEN_HEIGHT // 8
    tile_width      = SCREEN_WIDTH // 8
    height, width   = 8*tile_height, 8*tile_width
    background      = pygame.Surface((width, height))
    screen          = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Print the board
    print_board_background(background, colors, tile_height, tile_width)
    print_board_state(board, players, game_over, screen, tile_height, tile_width)

    # Game loop
    while not game_over:
        clock.tick(2)
        screen.fill([60, 70, 90])
        screen.blit(background, (0, 0))

        move_rule_counter = make_move(move_rule_counter, board, moves, players, whites_turn)
        game_over = is_game_over(move_rule_counter, board, moves, players)
        if move_done:
            whites_turn = not whites_turn
        print_board_state(board, players, game_over, screen, tile_height, tile_width)
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
