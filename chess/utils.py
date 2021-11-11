import itertools
import pygame
from defs import Board, Player, Piece, GRAY, PINK, SCREEN_HEIGHT, SCREEN_WIDTH
from move import check_move
from typing import List, Optional

def display_text(text: str, font_size: int, font_color: pygame.Color, display: pygame.Surface, x: int, y: int) -> None:
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text_surface = font.render(text, True, font_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    display.blit(text_surface, text_rect)

def print_board_background(background: pygame.Surface, colors: itertools.cycle, tile_height: int, tile_width: int) -> None:
    for y in range(0, SCREEN_HEIGHT, tile_height):
        for x in range(0, SCREEN_WIDTH, tile_width):
            rect = (x, y, tile_width, tile_height)
            pygame.draw.rect(background, next(colors), rect)
        next(colors)

def print_board_state(board: Board, players: List[Player], game_over: bool, display: pygame.Surface, tile_height: int, tile_width: int, whites_turn: bool) -> None:
    for x in range(8):
        for y in range(8):
            square  = board.squares[x][7-y]
            piece   = square.piece
            if piece is None:
                continue
            if square.highlighted:
                player = players[0] if whites_turn else players[1]
                highlight_piece(x, y, board, piece, player, display, tile_height, tile_width)
            display_piece(display, tile_height, tile_width, x, y, piece)

def highlight_square(x: int, y: int, board: Board, display: pygame.Surface, tile_height: int, tile_width: int) -> None:
    circle_coordinates = (x*tile_width + tile_width//2, (7-y)*tile_height + tile_height//2)
    if board.squares[x][y].piece is None:
        pygame.draw.circle(display, GRAY, circle_coordinates, tile_height/8)
    else:
        pygame.draw.circle(display, GRAY, circle_coordinates, tile_height//2, tile_height//6)
    if board.squares[x][y].piece is not None:
        display_piece(display, tile_height, tile_width, x, 7-y, board.squares[x][y].piece)

def highlight_possible_moves(board: Board, piece: Piece, player: Player, display: pygame.Surface, tile_height: int, tile_width: int) -> None:
    x_from, y_from = piece.location
    for y_to in range(8):
        for x_to in range(8):
            if check_move(x_from, y_from, x_to, y_to, board, player):
                highlight_square(x_to, y_to, board, display, tile_height, tile_width)

def display_piece(display: pygame.Surface, tile_height: int, tile_width: int, x: int, y: int, piece: Piece) -> None:
    piece_icon = pygame.image.load(piece.icon)
    piece_icon = pygame.transform.scale(piece_icon, (tile_width, tile_height))
    display.blit(piece_icon, (x*tile_width, y*tile_height))

def highlight_piece(x: int, y: int, board: Board, piece: Piece, player: Player, display: pygame.Surface, tile_height: int, tile_width: int) -> None:
    rect = (x*tile_width, y*tile_height, tile_width, tile_height)
    pygame.draw.rect(display, PINK, rect)
    highlight_possible_moves(board, piece, player, display, tile_height, tile_width)

def change_highlighted_piece(x: int, y: int, highlighted_piece: Piece, board: Board) -> Optional[Piece]:
    if highlighted_piece is not None:
        # Clear old highlight
        old_x, old_y = highlighted_piece.location
        board.squares[old_x][old_y].highlighted = False
        if board.squares[x][y].piece is not None and (
            (
                board.squares[x][y].piece.color != highlighted_piece.color
                or board.squares[x][y].piece == highlighted_piece
            )
        ):
            return None

    board.squares[x][y].highlighted = True
    return board.squares[x][y].piece