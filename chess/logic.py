from defs import Board, Move, Player
from typing import List

def is_checkmate():
    print("Checking for checkmate is not implemented")
    return False

def is_stalemate():
    print("Checking for stalemate is not implemented")
    return False

def is_game_over(move_rule_counter: int, board: Board, moves: List[Move], players: List[Player]) -> bool:
    if move_rule_counter >= 50:
        return True
    if is_checkmate():
        return True
    return is_stalemate()