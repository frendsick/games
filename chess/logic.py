from defs import Board, Move, Player
from typing import List

def is_checkmate(board: Board, white_player: Player, black_player: Player):
    # Position cannot be checkmate if none of the players are in check
    if not white_player.in_check and not black_player.in_check:
        return False

    print("Checking for checkmate is not implemented")
    return False

def is_stalemate(board: Board, white_player: Player, black_player: Player):
    print("Checking for stalemate is not implemented")
    return False

def is_game_over(move_rule_counter: int, board: Board, moves: List[Move], players: List[Player]) -> bool:
    if move_rule_counter >= 50:
        print("Game over - 50 move rule")
        return True
    white_player = players[0]
    black_player = players[1]
    if is_checkmate(board, white_player, black_player):
        return True
    return is_stalemate(board, white_player, black_player)