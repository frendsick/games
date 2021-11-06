from defs import Board, Location, Move, Piece, Player, Square
from move import is_legal_move
from typing import List

def get_squares_between_pieces(board: Board, checking_piece: Piece, target_location: Location) -> List[Square]:
    if checking_piece.type == 'KNIGHT':
        return []

    from_y, from_x          = checking_piece.location
    to_y, to_x              = target_location
    curr_x, curr_y          = from_x, from_y
    squares: List[Square]   = []

    for _ in range(max( abs(from_x - to_x)-1, abs(from_y - to_y)-1 )):
        if from_x != to_x:
            curr_x = curr_x+1 if from_x < to_x else curr_x-1
        if from_y != to_y:
            curr_y = curr_y+1 if from_y < to_y else curr_y-1
        curr_piece = board.squares[curr_x][curr_y].piece
        squares.append(Square(location=(curr_y, curr_x), piece=curr_piece))
    return squares

def is_checkmate(board: Board, player: Player):
    # Position cannot be checkmate if none of the players are in check
    if not player.in_check:
        return False

    # Map the squares between king and the checking pieces
    squares_between_king_and_checkers: List[List[Square]] = [] # Inner lists represent the different checking pieces
    for checking_piece in player.checking_pieces:
        target_location = board.king_locations[player.color.upper()]
        squares_between_king_and_checkers.append(get_squares_between_pieces(board, checking_piece, target_location))

    # Check if there is a move that escapes from the different checks
    for y in range(8):
        for x in range(8):
            piece = board.squares[x][y].piece
            if piece is None or piece.color != player.color.upper():
                continue
            # King can escape check by moving to a square that is not attacked
            if piece.type == 'KING':
                pass
            else:
                # Double check can not be blocked by a piece
                if len(squares_between_king_and_checkers) > 1:
                    continue
                # Check if the piece can occupy a square between the checker and the king
                for square in squares_between_king_and_checkers[0]:
                    x_from, y_from  = piece.location
                    x_to, y_to      = square.location
                    if is_legal_move(x_from, y_from, x_to, y_to, board, piece.color.upper()):
                        return False
    print("CHECKMATE")
    return True

def is_stalemate(board: Board, player: Player):
    print("Checking for stalemate is not implemented")
    return False

def is_game_over(move_rule_counter: int, board: Board, moves: List[Move], players: List[Player]) -> bool:
    if move_rule_counter >= 50:
        print("Game over - 50 move rule")
        return True

    # Only the player whose turn is next can be in checkmate or stalemate
    player = players[0] if len(moves)%2 == 0 else players[1]
    if is_checkmate(board, player):
        return True
    return is_stalemate(board, player)