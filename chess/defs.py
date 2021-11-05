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
    can_castle: bool = True

@dataclass
class Piece:
    id:    int
    color: str
    icon:  str # Unicode representation of a piece
    type:  str
    value: int

@dataclass
class Square:
    loc:    Tuple[int, int] # 1, 5 --> B6
    piece:  Piece = None
    oob:    bool  = False # Out of bounds square

@dataclass
class Move:
    from_square:    Square
    to_square:      Square
    moved_piece:    Piece
    captured_piece: Piece   = None

class Board:
    captured_pieces:    List[List[Piece]]
    moves:              List[Move]
    squares:            List[List[Square]]

    # Positive are white pieces, negative are black pieces
    # Zero's are empty, None's are out-of-bounds
    STARTING_POSITION = [
        [None]  * 10,
        [None]  * 10,
        [None, 50, 30, 31, 90, 9001, 31, 30, 50, None],
        [None, 10, 10, 10, 10, 10, 10, 10, 10, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, -10, -10, -10, -10, -10, -10, -10, -10, None],
        [None, -50, -30, -31, -90, -9001, -31, -30, -50, None],
        [None]  * 10,
        [None]  * 10
    ]

    def init_board(self) -> List[List[Square]]:
        import copy
        squares = copy.deepcopy(self.STARTING_POSITION) # Empty squares
        for x in range(10):
            for y in range(12):
                squares[y][x] = self.init_square(x, y)
        return squares

    def init_square(self, x, y) -> Square:
        if x < 2 or x > 9 or y < 1 or y > 8:
            return Square( loc=(y, x), piece=None, oob=True )

        if 3 < x < 8: # Empty square
            return Square( loc=(y, x), piece=None, oob=False )

        id      = y+(x*8)
        color   = 'WHITE' if x < 6 else 'BLACK'
        value   = abs(self.STARTING_POSITION[x][y])
        name    = PIECE_VALUE_MAP[value]
        icon    = PIECE_ICON_MAP[f'{color} {name}']
        piece   = Piece(id, color, icon, name, value)
        return Square( loc=(y, x), piece=piece, oob=False )

    def __init__(self) -> None:
        self.captured_pieces    = []
        self.moves              = []
        self.squares            = self.init_board()