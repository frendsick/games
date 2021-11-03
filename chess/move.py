import re
from typing import TextIO

from defs import Board

def invalid_move_error(move: str, error_message: str = None) -> None:
    print(f"'{move}' is not a valid move!")
    if error_message:
        print(error_message)

# Returns given move
def ask_move(turn: int) -> str:
    color       = 'White' if turn % 2 == 1 else 'Black'
    # move_regex  = r'[BRQNK][a-h][1-8]|[BRQNK][a-h]x[a-h][1-8]|[BRQNK][a-h][1-8]x[a-h][1-8]|[BRQNK][a-h][1-8][a-h][1-8]|[BRQNK][a-h][a-h][1-8]|[BRQNK]x[a-h][1-8]|[a-h]x[a-h][1-8]=(B+R+Q+N)|[a-h]x[a-h][1-8]|[a-h][1-8]x[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]x[a-h][1-8]|[a-h][1-8][a-h][1-8]=(B+R+Q+N)|[a-h][1-8][a-h][1-8]|[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]|[BRQNK][1-8]x[a-h][1-8]|[BRQNK][1-8][a-h][1-8]|O-O|O-O-O'
    move_regex = r'(?i)[a-h][1-8][a-h][1-8]' # Example: e2g4
    print(f"{color}'s turn!")
    while(True):
        print("Give move: ", end='')
        move = input()
        if re.fullmatch(move_regex, move) and move[:2] != move[-2:]:
            return move
        invalid_move_error(move)

def check_move(move: str, board: Board) -> bool:
    move_from   = move[:2]
    move_to     = move[-2:]

    invalid_move_error(move, "TEST")
    raise NotImplementedError

def move_piece(move: str, board: Board) -> Board:
    raise NotImplementedError

def make_move(board: Board, turn: int) -> Board:
    legal_move = False
    while not legal_move:
        move = ask_move(turn)
        legal_move = check_move(move, board)
    return move_piece(move, board)

def is_game_over():
    raise NotImplementedError
