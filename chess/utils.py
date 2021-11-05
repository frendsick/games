from defs import Board, Player
from typing import List

#     <Player2>
# 8   ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
# 7   ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
# 6   - - - - - - - -
# 5   - - - - - - - -
# 4   - - - - - - - -
# 3   - - - - - - - -
# 2   ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
# 1   ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
#     <Player1>
#     A B C D E F G H

def print_board(board: Board, players: List[Player]) -> None:
    print(f'\n    {players[1].name}', end='')
    for y in range(9, 1, -1):
        print(f'\n{y-1}  ', end='')
        for x in range(1,9):
            piece   = board.squares[x][y].piece
            icon    = '-' if piece is None else piece.icon
            print(f' {icon}', end='')
    print(f'\n    {players[0].name}')
    print('    A B C D E F G H\n')