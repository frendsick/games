import pygame
from defs import Board, Move, Player, GRAY, RED, SCREEN_HEIGHT, SCREEN_WIDTH
from move import can_piece_move
from typing import List
from utils import display_text

def legal_move_found(board: Board, player: Player) -> bool:
    for y in range(8):
        for x in range(8):
            piece = board.squares[x][y].piece
            if piece is None or piece.color != player.color.upper():
                continue

            # Check if piece can move to any square
            if can_piece_move(board, piece, player):
                return True
    return False

def is_checkmate(board: Board, player: Player) -> bool:
    # Position cannot be checkmate if none of the players are in check
    return bool(player.in_check and not legal_move_found(board, player))

# Stalemate is when a player is not in check but there is no legal moves
def is_stalemate(board: Board, player: Player) -> bool:
    return not legal_move_found(board, player)

def is_game_over(move_rule_counter: int, board: Board, moves: List[Move], players: List[Player], screen: pygame.Surface) -> bool:
    font_size = SCREEN_HEIGHT // 8
    message_x = SCREEN_WIDTH // 2
    message_y = int(SCREEN_HEIGHT/8*3.5)

    # Check for 50 move rule
    if move_rule_counter >= 50:
        display_text("Draw", font_size, GRAY, screen, message_x, message_y)
        print("Game over - 50 move rule")
        return True

    # Only the player whose turn is next can be in checkmate or stalemate
    player = players[0] if len(moves)%2 == 0 else players[1]
    if is_checkmate(board, player):
        display_text("Checkmate", font_size, RED, screen, message_x, message_y)
        return True
    if is_stalemate(board, player):
        display_text("Stalemate", font_size, GRAY, screen, message_x, message_y)
        return True