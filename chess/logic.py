from defs import Board, Location, Move, Piece, Player, Square
from move import check_move
from typing import List, Tuple

def legal_move_found(board: Board, player: Player) -> bool:
    for y in range(8):
        for x in range(8):
            piece = board.squares[x][y].piece
            if piece is None or piece.color != player.color.upper():
                continue

            # Check if piece can move to any square
            x_from, y_from = piece.location
            for x_to in range(8):
                for y_to in range(8):
                    if check_move(x_from, y_from, x_to, y_to, board, player):
                        return True
    return False

def is_checkmate(board: Board, player: Player) -> bool:
    # Position cannot be checkmate if none of the players are in check
    if not player.in_check or legal_move_found(board, player):
        return False
    print("Checkmate!")
    return True

# Stalemate is when a player is not in check but there is no legal moves
def is_stalemate(board: Board, player: Player) -> bool:
    if legal_move_found(board, player):
        return False
    print("Stalemate!")
    return True

def is_game_over(move_rule_counter: int, board: Board, moves: List[Move], players: List[Player]) -> bool:
    if move_rule_counter >= 50:
        print("Game over - 50 move rule")
        return True

    # Only the player whose turn is next can be in checkmate or stalemate
    player = players[0] if len(moves)%2 == 0 else players[1]
    if is_checkmate(board, player):
        return True
    return is_stalemate(board, player)