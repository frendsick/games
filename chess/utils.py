import pygame
from defs import Board, Player, SCREEN_HEIGHT, SCREEN_WIDTH
from typing import List

#     <Player2>
# 8   ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
# 7   ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
# 6   - - - - - - - -
# 5   - - - - - - - -
# 4   - - - - - - - -
# 3   - - - - - - - -
# 2   ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
# 1   ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
#     <Player1>
#     A B C D E F G H

def print_board(board: Board, players: List[Player], game_over) -> None:
    print(f'\n    {players[1].name}', end='')
    for y in range(7, -1, -1):
        print(f'\n{y+1}  ', end='')
        for x in range(8):
            piece   = board.squares[x][y].piece
            icon    = '-' if piece is None else piece.icon
            print(f' {icon}', end='')
    print(f'\n    {players[0].name}')
    print('    A B C D E F G H\n')
    if game_over:
        print("Game Over")
    elif players[0].in_check or players[1].in_check:
        print("CHECK!")

def print_board_background(background, colors, tile_height, tile_width):
    for y in range(0, SCREEN_HEIGHT, tile_height):
        for x in range(0, SCREEN_WIDTH, tile_width):
            rect = (x, y, tile_width, tile_height)
            pygame.draw.rect(background, next(colors), rect)
        next(colors)

def print_board_state(board: Board, players: List[Player], game_over: bool, display: pygame.Surface, tile_height: int, tile_width: int) -> None:
    for x in range(8):
        for y in range(8):
            piece   = board.squares[x][7-y].piece
            if piece is None:
                continue
            piece_icon = pygame.image.load(piece.icon)
            display.blit(piece_icon, (x*tile_width, y*tile_height))