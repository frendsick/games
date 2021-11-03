from defs import Board

# 8   ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
# 7   ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
# 6   - - - - - - - -
# 5   - - - - - - - -
# 4   - - - - - - - -
# 3   - - - - - - - -
# 2   ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
# 1   ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
#
#     A B C D E F G H

def print_board(board: Board) -> None:
    for y in range(8, 0, -1):
        print(f'\n{y}  ', end='')
        for x in range(1,9):
            piece   = board.squares[x][y].piece
            icon    = '-' if piece is None else piece.icon
            print(f' {icon}', end='')
    print('\n\n    A B C D E F G H\n')