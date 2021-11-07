from defs import Board, Location, Move, Piece, Player, Square
from move import check_move
from typing import List, Tuple

def get_squares_between_pieces(board: Board, checking_piece: Piece, target_location: Location) -> List[Square]:
    if checking_piece.type == 'KNIGHT':
        return []

    from_y, from_x          = checking_piece.location
    to_y, to_x              = target_location
    curr_x, curr_y          = from_x, from_y
    squares: List[Square]   = []

    for _ in range(max( abs(from_x - to_x)-1, abs(from_y - to_y)-1 )):
        curr_piece, curr_x, curr_y = get_square_between(from_y, from_x, to_y, to_x, curr_x, curr_y, board)
        squares.append(Square(location=(curr_x, curr_y), piece=curr_piece))
    return squares

def get_square_between(from_y: int, from_x: int, to_y: int, to_x: int, curr_x: int, curr_y: int, board: Board) -> Tuple[Piece, int, int]:
    if from_x != to_x:
        curr_x = curr_x+1 if from_x < to_x else curr_x-1
    if from_y != to_y:
        curr_y = curr_y+1 if from_y < to_y else curr_y-1
    curr_piece = board.squares[curr_y][curr_x].piece
    return curr_piece, curr_x, curr_y

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

            x_from, y_from = piece.location
            # King can escape check by moving to a square that is not attacked
            if piece.type == 'KING':
                # All possible directions starting from up and going clockwise
                possible_directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

                # Try moving to every square until a safe square is found
                for direction in possible_directions:
                    x_to = piece.location[0] + direction[0]
                    y_to = piece.location[1] + direction[1]
                    try:
                        if check_move(x_from, y_from, x_to, y_to, board, player):
                            return False
                    # IndexError happens if the king is at the edge of the board
                    except IndexError:
                        continue

            # All pieces except King
            else:
                # Double check can not be blocked by a piece
                if len(squares_between_king_and_checkers) > 1:
                    continue
                # Check if the piece can occupy a square between the checker and the king
                for square in squares_between_king_and_checkers[0]:
                    y_to, x_to = square.location
                    if check_move(x_from, y_from, x_to, y_to, board, player):
                        return False
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