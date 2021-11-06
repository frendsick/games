from defs import Board, Move, Player
from typing import List

def is_checkmate(board: Board, player: Player):
    # Position cannot be checkmate if none of the players are in check
    if not player.in_check:
        return False

    print("Checking for checkmate is not implemented")
    return False

def is_stalemate(board: Board, player: Player):
    print("Checking for stalemate is not implemented")
    return False

def is_game_over(move_rule_counter: int, board: Board, moves: List[Move], players: List[Player]) -> bool:
    if move_rule_counter >= 50:
        print("Game over - 50 move rule")
        return True

    # Only the player whose turn is next can be in checkmate or stalemate
    player = players[0] if len(moves)%2 == 0 else players[1]
    if is_checkmate(board, player):
        return True
    return is_stalemate(board, player)