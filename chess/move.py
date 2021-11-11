from copy import deepcopy
from typing import List, Tuple
from defs import Board, Move, Piece, Player, Square

# Checks if there is any legal moves available for the piece
def can_piece_move(board: Board, piece: Piece, player: Player) -> bool:
    x_from, y_from = piece.location
    for x_to in range(8):
        for y_to in range(8):
            if check_move(x_from, y_from, x_to, y_to, board, player):
                return True
    return False

def is_own_piece(x: int, y: int, board: Board, color: str) -> bool:
    piece = board.squares[x][y].piece
    if piece is not None:
        return piece.color == color.upper()
    return False

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
    home_row        = 1 if pawn.color == 'WHITE' else 6
    allowed_steps   = 2 if start_square.location[1] == home_row else 1
    right_direction = (y_from < y_to and pawn.color == 'WHITE') or (y_from > y_to and pawn.color == 'BLACK')

    # If the pawn walks forward check if there is any other pieces in the way
    if x_from == x_to and abs(y_from - y_to) <= allowed_steps and end_square.piece is None and right_direction:
        return not move_through_other_piece(x_from, y_from, x_to, y_to, board)
    # Capturing is only allowed diagonally
    if abs(x_from - x_to) == 1 and abs(y_from - y_to) == 1 and right_direction:
        # Diagonal movement is only allowed when capturing
        if end_square.piece is not None and pawn.color != end_square.piece:
            return True

        # Check en passant
        if x_from - x_to < 0: # If en passanting to the right
            if board.squares[x_from+1][y_from].piece is not None and board.squares[x_from+1][y_from].piece.en_passant is True:
                return True
        elif board.squares[x_from-1][y_from].piece is not None and board.squares[x_from-1][y_from].piece.en_passant is True:
            return True
    return False

def legal_knight_move(x_from: int, y_from: int, x_to: int, y_to: int) -> bool:
    x_diff = abs(x_from - x_to)
    y_diff = abs(y_from - y_to)
    return (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2)

def legal_bishop_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    # Bishop should move diagonally
    if abs(x_from-x_to) != abs(y_from-y_to):
        return False
    return not move_through_other_piece(x_from, y_from, x_to, y_to, board)

def legal_rook_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    # Rook can only move horizontally or vertically
    if x_from != x_to and y_from != y_to:
        return False
    return not move_through_other_piece(x_from, y_from, x_to, y_to, board)

def legal_queen_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    # Queen can move to any direction
    if (
        x_from != x_to and y_from != y_to
        and abs(x_from - x_to) != abs(y_from - y_to)
    ):
        return False
    return not move_through_other_piece(x_from, y_from, x_to, y_to, board)

# Move the rook two squares. King move will be done afterwards.
def castle(board: Board, y: int, castle_right: bool) -> Board:
    if castle_right:
        board.squares[5][y].piece == board.squares[7][y].piece
        board.squares[7][y].piece == None
    else:
        board.squares[2][y].piece == board.squares[0][y].piece
        board.squares[0][y].piece == None
    return board

def legal_king_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board) -> bool:
    king    = board.squares[x_from][y_from].piece
    # Check castling
    # TODO: Prevent castling through check
    if (king.can_castle and abs(x_from - x_to) == 2 and y_from == y_to
        and not move_through_other_piece(x_from, y_from, x_to, y_to, board)):
        if x_from > x_to and board.squares[0][y_from].piece is not None:
            return board.squares[0][y_from].piece.can_castle
        elif x_from < x_to and board.squares[7][y_from].piece is not None:
            return board.squares[7][y_from].piece.can_castle

    # King can move to any direction but only one step
    if abs(x_from - x_to) > 1 or abs(y_from - y_to) > 1:
        return False
    if (
        x_from != x_to and y_from != y_to
        and abs(x_from - x_to) != abs(y_from - y_to)
    ):
        return False
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
        return legal_knight_move(x_from, y_from, x_to, y_to)
    if moved_piece.type == "BISHOP":
        return legal_bishop_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "ROOK":
        return legal_rook_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "QUEEN":
        return legal_queen_move(x_from, y_from, x_to, y_to, board)
    if moved_piece.type == "KING":
        return legal_king_move(x_from, y_from, x_to, y_to, board)
    raise RuntimeError("This should not be accessible")

def get_checking_pieces(board: Board, player: Player) -> List[Piece]:
    checking_pieces: List[Piece] = []
    for y in range(8):
        for x in range(8):
            piece = board.squares[x][y].piece
            # Player's pieces cannot check own king
            if piece is None or piece.color == player.color.upper():
                continue
            # Check if the current piece can get to the opponent's king
            target_king_x, target_king_y = board.king_locations[player.color.upper()]
            if is_legal_move(x, y, target_king_x, target_king_y, board, piece.color):
                checking_pieces.append(board.squares[x][y].piece)
    return checking_pieces

def move_piece(x_from: int, y_from: int, x_to: int, y_to: int, move_rule_counter: int, players: List[Player], board: Board, moves: List[Move]) -> int:
    moved_piece     = board.squares[x_from][y_from].piece
    target_piece    = board.squares[x_to][y_to].piece
    captured_piece  = target_piece if target_piece != None else None
    from_square     = Square( (x_from, y_from), moved_piece )
    to_square       = Square( (x_to, y_to), target_piece )
    move_rule_counter += 1

    # If castling, move the corresponding rook over the king
    if moved_piece.type == 'KING':
        board = check_for_castling(x_from, y_from, x_to, players, board, moves, to_square)
    # Moving pawn resets the 50 move rule counter
    if moved_piece.type == 'PAWN':
        move_rule_counter   = 0
        queening_row        = 7 if moved_piece.color == 'WHITE' else 0
        # Pawn becomes a queen if it gets to the other end of the board
        # TODO: Underpromotion
        if y_to == queening_row:
            moved_piece.type = 'QUEEN'
            moved_piece.icon = f'icons/{moved_piece.color}_QUEEN.png'
        # If moving pawn two squares forwards change en_passant boolean to true for the next turn
        if abs(y_from - y_to) == 2:
            moved_piece.en_passant = True
        # If en passanting the target pawn is right next to the from_square
        if abs(x_from - x_to) == 1 and target_piece is None:
            board.squares[x_from-(x_from-x_to)][y_from].piece = None
    # Capturing a piece resets the 50 move rule counter
    if captured_piece:
        move_rule_counter = 0

    moves = do_move(x_from, y_from, x_to, y_to, board, moves, moved_piece, captured_piece, from_square, to_square)
    update_players_in_check(board, moves, players)

    return move_rule_counter

def update_players_in_check(board: Board, moves: List[Move], players: List[Player]) -> None:
    player          = players[ (len(moves)+1)%2 ]
    opponent        = players[ len(moves)%2 ]
    checking_pieces = get_checking_pieces(board, opponent)
    if checking_pieces != []:
        opponent.checking_pieces = checking_pieces
        opponent.in_check = True
    player.in_check = False

def do_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board, moves: List[Move], moved_piece: Piece, captured_piece: Piece, from_square: Square, to_square: Square) -> List[Move]:
    moves.append( Move(from_square, to_square, moved_piece, captured_piece) )
    moved_piece.location = (x_to, y_to)
    board.squares[x_to][y_to].piece = moved_piece
    board.squares[x_from][y_from].piece = None
    return moves

def check_for_castling(x_from: int, y_from: int, x_to: int, players: List[Player], board: Board, moves: List[Move], to_square: Square):
    board.king_locations[players[len(moves)%2].color.upper()] = to_square.location
    if abs(x_from - x_to) == 2:
        board = move_rook_when_castling(x_from, y_from, x_to, board)
    return board

def move_rook_when_castling(x_from: int, y_from: int, x_to: int, board: Board) -> Board:
    if x_from < x_to:
        return do_rook_move_when_castling(7, y_from, 5, board)
    else:
        return do_rook_move_when_castling(0, y_from, 3, board)

def do_rook_move_when_castling(x_from: int, y_from: int, x_to: int, board: Board) -> Board:
    source_square = board.squares[x_from][y_from]
    target_square = board.squares[x_to][y_from]
    target_square.piece = source_square.piece
    target_square.piece.location = (x_to, y_from)
    target_square.highlighted = False
    source_square.piece = None
    return board

def moving_results_in_check(x_from, y_from, x_to, y_to, board, player):
    board_copy = deepcopy(board)
    board_copy.squares[x_to][y_to].piece = board_copy.squares[x_from][y_from].piece
    board_copy.squares[x_from][y_from].piece = None
    if board_copy.squares[x_to][y_to].piece.type == 'KING':
        board_copy.king_locations[player.color.upper()] = (x_to, y_to)
    return get_checking_pieces(board_copy, player) != []

def check_move(x_from: int, y_from: int, x_to: int, y_to: int, board: Board, player: Player) -> bool:
    if not is_own_piece(x_from, y_from, board, player.color):
        return False
    if not is_legal_move(x_from, y_from, x_to, y_to, board, player.color):
        return False
    return not moving_results_in_check(x_from, y_from, x_to, y_to, board, player)

def clear_en_passant(board: Board, moves: List[Move]) -> Board:
    if len(moves) > 1:
        x_prev, y_prev = moves[-2].to_square.location
        if board.squares[x_prev][y_prev].piece != None:
            board.squares[x_prev][y_prev].piece.en_passant = False
    return board

# Makes move and returns the 50 move rule counter
def make_move(x_from: int, y_from: int, x_to: int, y_to: int, move_rule_counter: int, board: Board, moves: List[Move], players: List[Player], whites_turn: bool, debug=False, debug_game=None) -> Tuple[bool, int]:
    player: Player = players[0] if whites_turn else players[1] # players[0] => White

    if not check_move(x_from, y_from, x_to, y_to, board, player):
        print("Illegal move:", (x_from, y_from), "=>", (x_to, y_to))
        return False, move_rule_counter

    # Revocate castling rights when moving king or rook
    piece = board.squares[x_from][y_from].piece
    if piece.type in ['KING', 'ROOK']:
        piece.can_castle = False

    # Clear en passant for the previous move
    board = clear_en_passant(board, moves)
    
    return True, move_piece(x_from, y_from, x_to, y_to, move_rule_counter, players, board, moves)
