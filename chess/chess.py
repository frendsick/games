#!/usr/bin/python3
import itertools
import pygame
from typing import List
from defs   import Board, Move, Piece, Player, BLACK, WHITE, MOUSE_BUTTONS, TICKRATE, SCREEN_HEIGHT, SCREEN_WIDTH
from logic  import is_game_over
from move   import make_move, undo_move
from utils  import change_highlighted_piece, print_board_background, print_board_state

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
    background      = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen          = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Print the board
    print_board_background(background, colors, tile_height, tile_width)
    print_board_state(board, players, game_over, screen, tile_height, tile_width, whites_turn)

    # Game loop
    while not game_over:
        move_done = False
        clock.tick(TICKRATE)
        fill_screen(background, screen)
        events: List[pygame.event.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == MOUSE_BUTTONS['LEFT']:
                    mouse_pos           = pygame.mouse.get_pos()
                    x_to, y_to          = mouse_pos[0] // tile_width , 7 - (mouse_pos[1] // tile_height)
                    if highlighted_piece is not None:
                        x_from, y_from  = highlighted_piece.location
                        move_done, move_rule_counter = make_move(x_from, y_from, x_to, y_to, move_rule_counter, board, moves, players, whites_turn)
                    highlighted_piece   = change_highlighted_piece(x_to, y_to, highlighted_piece, board)
                elif event.button == MOUSE_BUTTONS['RIGHT']:
                    print("Right click")
            # Undo the last move with CTRZ-Z or U
            if (
                event.type == pygame.KEYDOWN and
                moves                       and
                (event.key == pygame.K_u    or
                (event.key == pygame.K_z    and
                pygame.key.get_mods()       and
                pygame.KMOD_CTRL))
            ):
                undo_move(board, moves)
                if move_rule_counter > 0:
                    move_rule_counter -= 1
                move_done = True

        game_over = is_game_over(move_rule_counter, board, moves, players)
        if move_done:
            whites_turn = not whites_turn
        print_board_state(board, players, game_over, screen, tile_height, tile_width, whites_turn)
        pygame.display.update()
    print("Game over")

def fill_screen(background: pygame.Surface, screen: pygame.Surface) -> None:
    screen.fill([60, 70, 90])
    screen.blit(background, (0, 0))

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
