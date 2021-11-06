from dataclasses import dataclass
from typing import List, Tuple

PIECE_VALUE_MAP = {
    10:     'PAWN',
    30:     'KNIGHT',
    31:     'BISHOP',
    50:     'ROOK',
    90:     'QUEEN',
    9001:   'KING'
}

PIECE_ICON_MAP = {
    'BLACK KING'    : '\u2654',
    'BLACK QUEEN'   : '\u2655',
    'BLACK ROOK'    : '\u2656',
    'BLACK BISHOP'  : '\u2657',
    'BLACK KNIGHT'  : '\u2658',
    'BLACK PAWN'    : '\u2659',
    'WHITE KING'    : '\u265A',
    'WHITE QUEEN'   : '\u265B',
    'WHITE ROOK'    : '\u265C',
    'WHITE BISHOP'  : '\u265D',
    'WHITE KNIGHT'  : '\u265E',
    'WHITE PAWN'    : '\u265F',
}

@dataclass
class Player:
    color: str
    name: str
    rating: int

@dataclass
class Piece:
    id:    int
    color: str
    icon:  str # Unicode representation of a piece
    type:  str
    value: int
    can_castle: bool # Variable for King and Rook objects
    en_passant: bool = None # If the pawn can be captured en passant this turn

Location = Tuple[int, int]

@dataclass
class Square:
    loc:    Location # 1, 5 --> B6
    piece:  Piece = None

@dataclass
class Move:
    from_square:    Square
    to_square:      Square
    moved_piece:    Piece
    captured_piece: Piece   = None

class Board:
    captured_pieces:    List[List[Piece]]
    king_locations:     List[Location]
    moves:              List[Move]
    squares:            List[List[Square]]

    # Positive are white pieces, negative are black pieces
    # Zero's are empty, None's are out-of-bounds
    STARTING_POSITION = [
        [ 50, 30, 31, 90, 9001, 31, 30, 50 ],
        [ 10, 10, 10, 10, 10, 10, 10, 10 ],
        [ 0, 0, 0, 0, 0, 0,  0, 0 ],
        [ 0, 0, 0, 0, 0, 0,  0, 0 ],
        [ 0, 0, 0, 0, 0, 0,  0, 0 ],
        [ 0, 0, 0, 0, 0, 0,  0, 0 ],
        [ -10, -10, -10, -10, -10, -10, -10, -10 ],
        [ -50, -30, -31, -90, -9001, -31, -30, -50 ]
    ]

    def init_board(self) -> List[List[Square]]:
        import copy
        squares = copy.deepcopy(self.STARTING_POSITION) # Empty squares
        for x in range(8):
            for y in range(8):
                squares[y][x] = self.init_square(x, y)
        return squares

    def init_square(self, x, y) -> Square:
        if 1 < x < 6: # Empty square
            return Square( loc=(y, x), piece=None)

        id          = y+(x*8)
        color       = 'WHITE' if x < 5 else 'BLACK'
        value       = abs(self.STARTING_POSITION[x][y])
        type        = PIECE_VALUE_MAP[value]
        icon        = PIECE_ICON_MAP[f'{color} {type}']
        can_castle  = type in ['KING', 'ROOK']
        piece       = Piece(id, color, icon, type, value, can_castle)
        return Square( loc=(y, x), piece=piece)

    def __init__(self) -> None:
        self.captured_pieces    = []
        self.king_locations     = [ (4,0), (4,7) ]
        self.moves              = []
        self.squares            = self.init_board()