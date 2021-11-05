import re
from typing import List, TextIO, Tuple

from defs import Board, Move, Square, Piece
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
            move_from = (int(ord(move[0])-64), int(move[1])+1)
            move_to = (int(ord(move[2]) - 64), int(move[3])+1)
            return move_from, move_to
        invalid_move_error(move)

def is_own_piece(x: int, y: int, board: Board, color: str) -> bool:
    piece = board.squares[x][y].piece
    return piece is not None or piece.color != color.upper()

def in_check(loc_from: Tuple[int, int], loc_to: Tuple[int, int], board: Board) -> bool:
    raise NotImplementedError

def move_through_other_piece(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    x_curr = x_from
    y_curr = y_from

    while (abs(x_to-x_curr) > 1 or abs(y_to-y_curr) > 1):
        if x_from != x_to:
            x_curr = x_curr+1 if x_to > x_from else x_curr-1
        if y_from != y_to:
            y_curr = y_curr+1 if y_to > y_from else y_curr-1
        if board.squares[x_curr][y_curr].piece != None:
            return True
    return False

def legal_pawn_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    start_square    = board.squares[x_from][y_from]
    end_square      = board.squares[x_to][y_to]
    pawn            = start_square.piece
    home_row        = 3 if pawn.color == 'WHITE' else 8
    allowed_steps   = 2 if start_square.loc[1] == home_row else 1
    right_direction = (y_from < y_to and pawn.color == 'WHITE') or (y_from > y_to and pawn.color == 'BLACK')

    # If the pawn walks forward check if there is any other pieces in the way
    if x_from == x_to and abs(y_from - y_to) <= allowed_steps and end_square.piece is None and right_direction:
        return not move_through_other_piece(x_from, y_from, x_to, y_to, board)
    # Capturing is only allowed diagonally
    if abs(x_from - x_to) == 1 and abs(y_from - y_to) == 1 and right_direction:
        return end_square.piece is not None and pawn.color != end_square.piece
    return False

def legal_knight_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    start_square    = board.squares[x_from][y_from]
    end_square      = board.squares[x_to][y_to]
    knight          = start_square.piece

    print("Knight move rules are not implemented!")
    return True

def legal_bishop_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    start_square    = board.squares[x_from][y_from]
    end_square      = board.squares[x_to][y_to]
    bishop          = start_square.piece
    # Bishop should move diagonally
    if abs(x_from-x_to) != abs(y_from-y_to):
        return False
    return not move_through_other_piece(x_from, y_from, x_to, y_to, board)

def legal_rook_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    start_square    = board.squares[x_from][y_from]
    end_square      = board.squares[x_to][y_to]
    rook            = start_square.piece

    print("Rook move rules are not implemented!")
    return True

def legal_queen_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    start_square    = board.squares[x_from][y_from]
    end_square      = board.squares[x_to][y_to]
    queen           = start_square.piece

    print("Queen move rules are not implemented!")
    return True

def legal_king_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    start_square    = board.squares[x_from][y_from]
    end_square      = board.squares[x_to][y_to]
    king            = start_square.piece

    print("King move rules are not implemented!")
    return True

def is_legal_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board, color: str) -> bool:
    moved_piece     = board.squares[x_from][y_from].piece
    target_piece    = board.squares[x_to][y_to].piece

    # Cannot capture own piece
    if target_piece is not None and target_piece.color == color.upper():
        return False

    # Check is the move legal for the type of the piece
    if moved_piece.type == "PAWN":
        return legal_pawn_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "KNIGHT":
        return legal_knight_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "BISHOP":
        return legal_bishop_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "ROOK":
        return legal_rook_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "QUEEN":
        return legal_queen_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "KING":
        return legal_king_move(x_from, y_from, x_to, y_to, board)
    raise RuntimeError("This should not be accessible")

def move_piece(x_from: int, y_from: int, x_to: int, y_to: int, board: Board, moves: List[Move]) -> Board:
    # TODO: Move rules for different pieces
    moved_piece     = board.squares[x_from][y_from].piece
    target_piece    = board.squares[x_to][y_to].piece
    captured_piece  = target_piece if target_piece != None else None
    from_square     = Square( (x_from, y_from), moved_piece )
    to_square       = Square( (x_to, y_to), target_piece )

    moves.append( Move(from_square, to_square, moved_piece, captured_piece) )
    board.squares[x_to][y_to].piece = moved_piece
    board.squares[x_from][y_from].piece = None
    return board

def check_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board, color: int) -> bool:
    if not is_own_piece(x_from, y_from, board, color):
        return False
    return is_legal_move(x_from, y_from, x_to, y_to, board, color)

def make_move(board: Board, moves: List[Move], turn: int) -> Board:
    color: str = 'White' if turn % 2 == 1 else 'Black'
    legal_move = False
    while not legal_move:
        move_from, move_to = ask_move(color)
        x_from, y_from  = move_from
        x_to,   y_to    = move_to
        legal_move = check_move(x_from, y_from, x_to, y_to, board, color)
    return move_piece(x_from, y_from, x_to, y_to, board, moves)

def is_game_over():
    raise NotImplementedError
