#!/usr/bin/python3
import itertools
import pygame
from typing import List, Tuple
from defs   import Board, Move, Piece, Player, BLACK, GRAY, WHITE, MOUSE_BUTTONS, TICKRATE, SCREEN_HEIGHT, SCREEN_WIDTH
from logic  import is_game_over
from move   import make_move, undo_move
from utils  import change_highlighted_piece, display_text, print_board_background, print_board_state

def new_game(background: pygame.Surface, screen: pygame.Surface) -> None:
    game_over: bool             = False
    highlighted_piece: Piece    = None
    whites_turn: bool           = True
    move_rule_counter: int      = 0 # 50 move rule
    players: List[Player]       = [Player("White", "CyberPaddy", 1337), Player("Black", "Random n00b", 420)]
    board                       = Board() # Initializes the board to the starting position
    moves: List[Move]           = []

    # Pygame variables
    clock           = pygame.time.Clock()
    colors          = itertools.cycle((WHITE, BLACK))
    tile_height     = SCREEN_HEIGHT // 8
    tile_width      = SCREEN_WIDTH  // 8

    # Print the board
    print_board_background(background, colors, tile_height, tile_width)
    print_board_state(board, players, screen, tile_height, tile_width, whites_turn)

    while not game_over:
        clock.tick(TICKRATE)
        game_over, background, screen, highlighted_piece, whites_turn, move_rule_counter, players, moves = \
            game_loop(background, screen, highlighted_piece, whites_turn, move_rule_counter, players, board, moves, tile_height, tile_width)

def game_loop(background: pygame.Surface, screen: pygame.Surface, highlighted_piece: Piece, whites_turn: bool, move_rule_counter: int, players: List[Player], board: Board, moves: List[Move], tile_height: int, tile_width: int) \
    -> Tuple[bool, pygame.Surface, pygame.Surface, Piece, bool, int, List[Player], List[Move]]:
    # Draw the background
    fill_screen(background, screen)

    events: List[pygame.event.Event] = pygame.event.get()
    move_done: bool = False
    for event in events:
        if move_done:
            break
        highlighted_piece, whites_turn, move_done, move_rule_counter, players, moves = \
            handle_event(highlighted_piece, whites_turn, move_done, move_rule_counter, players, board, moves, tile_height, tile_width, event)

    game_over = is_game_over(move_rule_counter, board, moves, players, screen)

    if move_done:
        whites_turn = not whites_turn

    # Display the new board state and return
    print_board_state(board, players, screen, tile_height, tile_width, whites_turn)
    pygame.display.update()
    return game_over, background, screen, highlighted_piece, whites_turn, move_rule_counter, players, moves

def handle_event(highlighted_piece: Piece, whites_turn: bool, move_done: bool, move_rule_counter: int, players: List[Player], board: Board, moves: List[Move], tile_height: int, tile_width: int, event: pygame.event.Event) \
    -> Tuple[Piece, bool, bool, int, List[Player], List[Move]]:
    if event.type == pygame.QUIT:
        exit(0)

    move_done = False
    if (
        event.type == pygame.MOUSEBUTTONDOWN
        and event.button == MOUSE_BUTTONS['LEFT']
    ):
        mouse_pos           = pygame.mouse.get_pos()
        x_to, y_to          = mouse_pos[0] // tile_width , 7 - (mouse_pos[1] // tile_height)
        if highlighted_piece is not None:
            x_from, y_from  = highlighted_piece.location
            move_done, move_rule_counter = make_move(x_from, y_from, x_to, y_to, move_rule_counter, board, moves, players, whites_turn)
        highlighted_piece   = change_highlighted_piece(x_to, y_to, highlighted_piece, board)

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
    return highlighted_piece, whites_turn, move_done, move_rule_counter, players, moves

def fill_screen(background: pygame.Surface, screen: pygame.Surface) -> None:
    screen.fill([60, 70, 90])
    screen.blit(background, (0, 0))

def play_again(screen: pygame.Surface) -> None:
    font_size = SCREEN_WIDTH // 18
    text_x    = SCREEN_WIDTH // 2
    text_y    = int(SCREEN_HEIGHT // 8 * 5.5)
    display_text("Play again? (Y/N)", font_size, GRAY, screen, text_x, text_y)
    pygame.display.update()

    # Wait for Y or N press from the user
    while(True):
        events: List[pygame.event.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                return True

def main():
    pygame.init()
    background  = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen      = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    playing     = True
    while playing:
        new_game(background, screen)
        playing = play_again(screen)

if __name__ == '__main__':
    main()
