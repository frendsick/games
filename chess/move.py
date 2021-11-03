import re
from typing import TextIO

from defs import Board, Piece

def invalid_move_error(move: str, error_message: str = None) -> None:
    print(f"'{move}' is not a valid move!")
    if error_message:
        print(error_message)

# Returns given move
def ask_move(color: str) -> str:
    # move_regex  = r'[BRQNK][a-h][1-8]|[BRQNK][a-h]x[a-h][1-8]|[BRQNK][a-h][1-8]x[a-h][1-8]|[BRQNK][a-h][1-8][a-h][1-8]|[BRQNK][a-h][a-h][1-8]|[BRQNK]x[a-h][1-8]|[a-h]x[a-h][1-8]=(B+R+Q+N)|[a-h]x[a-h][1-8]|[a-h][1-8]x[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]x[a-h][1-8]|[a-h][1-8][a-h][1-8]=(B+R+Q+N)|[a-h][1-8][a-h][1-8]|[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]|[BRQNK][1-8]x[a-h][1-8]|[BRQNK][1-8][a-h][1-8]|O-O|O-O-O'
    move_regex = r'(?i)[a-h][1-8][a-h][1-8]' # Example: e2g4
    print(f"{color}'s turn!")
    while(True):
        print("Give move: ", end='')
        move = input()
        if re.fullmatch(move_regex, move) and move[:2] != move[-2:]:
            return move.upper()
        invalid_move_error(move)

def is_own_piece(x: int, y: int, board: Board, color: str) -> bool:
    piece = board.squares[x][y].piece
    print(piece is None)
    print(piece.color == color.upper())
    return piece is None or piece.color != color.upper()

def check_move(move: str, board: Board, color: int) -> bool:
    assert len(move) == 4, "Error in move parsing"
    x_from  = int(ord(move[0]) - 64)
    y_from  = int(move[1])
    x_to    = int(ord(move[2]) - 64)
    y_to    = int(move[1])
    print(x_from, y_from, x_to, y_to)
    if not is_own_piece(x_from, y_from, board, color):
        return False

    invalid_move_error(move, "TEST")
    raise NotImplementedError

def move_piece(move: str, board: Board) -> Board:
    raise NotImplementedError

def make_move(board: Board, turn: int) -> Board:
    color: str = 'White' if turn % 2 == 1 else 'Black'
    legal_move = False
    while not legal_move:
        move = ask_move(color)
        legal_move = check_move(move, board, color)
    return move_piece(move, board)

def is_game_over():
    raise NotImplementedError
