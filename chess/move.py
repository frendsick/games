import re
from typing import List, TextIO, Tuple

from defs import Board, Move, Square
from utils import print_board

def invalid_move_error(move: str, error_message: str = None) -> None:
    print(f"'{move}' is not a valid move!")
    if error_message:
        print(error_message)

# Returns given move in two tuples of coordinates for the move
def ask_move(color: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    # move_regex  = r'[BRQNK][a-h][1-8]|[BRQNK][a-h]x[a-h][1-8]|[BRQNK][a-h][1-8]x[a-h][1-8]|[BRQNK][a-h][1-8][a-h][1-8]|[BRQNK][a-h][a-h][1-8]|[BRQNK]x[a-h][1-8]|[a-h]x[a-h][1-8]=(B+R+Q+N)|[a-h]x[a-h][1-8]|[a-h][1-8]x[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]x[a-h][1-8]|[a-h][1-8][a-h][1-8]=(B+R+Q+N)|[a-h][1-8][a-h][1-8]|[a-h][1-8]=(B+R+Q+N)|[a-h][1-8]|[BRQNK][1-8]x[a-h][1-8]|[BRQNK][1-8][a-h][1-8]|O-O|O-O-O'
    move_regex = r'(?i)[a-h][1-8][a-h][1-8]' # Example: e2g4
    print(f"{color}'s turn!")
    while(True):
        print("Give move: ", end='')
        move = input().upper()
        if re.fullmatch(move_regex, move) and move[:2] != move[-2:]:
            move_from = (int(ord(move[0])-64), int(move[1]))
            move_to = (int(ord(move[2]) - 64), int(move[3]))
            return move_from, move_to
        invalid_move_error(move)

def is_own_piece(loc: Tuple[int, int], board: Board, color: str) -> bool:
    piece = board.squares[loc[0]][loc[1]].piece
    return piece is not None or piece.color != color.upper()

def move_piece(loc_from: Tuple[int, int], loc_to: Tuple[int, int], board: Board, moves: List[Move]) -> Board:
    # TODO: Move rules for different pieces
    x_from, y_from  = loc_from
    x_to,   y_to    = loc_to
    moved_piece     = board.squares[x_from][y_from].piece
    target_piece    = board.squares[x_to][y_to].piece
    captured_piece  = target_piece if target_piece != None else None
    from_square     = Square( (loc_from), moved_piece )
    to_square       = Square( (loc_to), target_piece )

    moves.append( Move(from_square, to_square, moved_piece, captured_piece) )
    board.squares[x_to][y_to].piece = moved_piece
    board.squares[x_from][y_from].piece = None
    return board

def check_move(move_from: Tuple[int, int], move_to: Tuple[int, int], board: Board, color: int) -> bool:
    return is_own_piece(move_from, board, color)

def make_move(board: Board, moves: List[Move], turn: int) -> Board:
    color: str = 'White' if turn % 2 == 1 else 'Black'
    legal_move = False
    while not legal_move:
        move_from, move_to = ask_move(color)
        legal_move = check_move(move_from, move_to, board, color)
    return move_piece(move_from, move_to, board, moves)

def is_game_over():
    raise NotImplementedError
