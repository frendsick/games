from dataclasses import dataclass
from typing import List, Tuple

PIECE_MAP = {
    10:     'Pawn',
    30:     'Knight',
    31:     'Bishop',
    50:     'Rook',
    90:     'Queen',
    9001:   'King'
}

@dataclass
class Piece:
    id:    int
    color: str
    name:  str
    value: int

@dataclass
class Square:
    loc: Tuple[int, int] # 1, 5 --> B6
    piece: Piece = None

class Board:
    # Positive are white pieces, negative are black pieces
    STARTING_POSITION = [ \
        [-50, -30, -31, -90, -9001, -31, -30, -50], \
        [-10] * 8, \
        [0]   * 8, \
        [0]   * 8, \
        [0]   * 8, \
        [0]   * 8, \
        [10]  * 8, \
        [50, 30, 31, 90, 9001, 31, 30, 50] \
    ]

    def init_board(self) -> List[Square]:
        squares = [] # Empty squares
        for x in range(8):
            for y in range(8):
                squares.append(self.init_square(x, y))
        return squares

    def init_square(self, x, y) -> Square:
        if 1 < x < 6: # Empty square
            return Square( (x, y) )

        id      = y+(x*8)
        color   = 'WHITE' if x < 6 else 'BLACK'
        value   = abs(self.STARTING_POSITION[x][y])
        name    = PIECE_MAP[value]
        piece   = Piece(id, color, name, value)
        return Square( (x, y), piece )

    def __init__(self) -> None:
        self.squares: List[List[Square]] = self.init_board() # 8*8 Squares