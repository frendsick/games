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
class Piece:
    id:    int
    color: str
    icon:  str # Unicode representation of a piece
    name:  str
    value: int

@dataclass
class Square:
    loc:    Tuple[int, int] # 1, 5 --> B6
    piece:  Piece = None
    oob:    bool  = False # Out of bounds square

class Board:
    captured_pieces:    List[List[Piece]]
    squares:            List[List[Square]]

    # Positive are white pieces, negative are black pieces
    # Zero's are empty, None's are out-of-bounds
    STARTING_POSITION = [
        [None]  * 10,
        [None, -50, -30, -31, -90, -9001, -31, -30, -50, None],
        [None, -10, -10, -10, -10, -10, -10, -10, -10, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, 0, 0, 0, 0, 0, 0,  0, 0, None],
        [None, 10, 10, 10, 10, 10, 10, 10, 10, None],
        [None, 50, 30, 31, 90, 9001, 31, 30, 50, None],
        [None]  * 10
    ]

    def init_board(self) -> List[List[Square]]:
        squares = self.STARTING_POSITION # Empty squares
        for x in range(10):
            for y in range(10):
                squares[x][y] = self.init_square(x, y)
        return squares

    def init_square(self, x, y) -> Square:
        if x < 1 or x > 8 or y < 1 or y > 8:
            return Square( loc=(x, y), piece=None, oob=True )

        if 2 < x < 7: # Empty square
            return Square( loc=(x, y), piece=None, oob=False )

        id      = y+(x*8)
        color   = 'BLACK' if x < 6 else 'WHITE'
        value   = abs(self.STARTING_POSITION[x][y])
        name    = PIECE_VALUE_MAP[value]
        icon    = PIECE_ICON_MAP[f'{color} {name}']
        piece   = Piece(id, color, icon, name, value)
        return Square( loc=(x, y), piece=piece, oob=False )

    def __init__(self) -> None:
        self.captured_pieces    = []
        self.squares            = self.init_board()