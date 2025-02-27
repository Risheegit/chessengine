"""
Functions for generating moves for all supported pieces in all supported scenarios
"""


from chessengine.utils import get_rank, get_file

HIGHEST_SQUARE = 2**63


def check_valid_position(
    board,
    side: str,
    start: int,
    end: int,
    moves: list[tuple[int, int]],
    auto_add: bool = True,
) -> tuple[bool, bool]:
    """
    Returns a tuple(bool). The first value indicates whether
    this position is valid to move to, the second indicates
    whether this is the last valid position in the direction
    that the piece is currently moving (whether the piece
    should try to explore the next position in the direction
    that is being explored)

    If auto_add is True, adds the position to the moves list
    if the move is valid
    """
    if end > HIGHEST_SQUARE:
        return False, True
    if end <= 0:
        return False, True
    if end & board.all_pieces == 0:
        if auto_add:
            moves.append((start, end))
        return True, False
    elif side == "white" and end & board.all_white == 0:
        if auto_add:
            moves.append((start, end))
        return True, True
    elif side == "black" and end & board.all_black == 0:
        if auto_add:
            moves.append((start, end))
        return True, True
    else:
        return False, True


def get_rook_moves(board, side: str, position: int) -> list[int]:
    """
    Returns a list of end positions a rook of side=side can reach starting at position
    """
    moves = []

    _ = position
    while True:
        # Move rank up
        _ = _ << 8
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    _ = position
    while True:
        # Move rank down
        _ = _ >> 8
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    file = get_file(position)
    max_right = 8 - file
    _ = position
    for i in range(max_right):
        # Move right
        _ = _ << 1
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    max_left = file - 1
    _ = position
    for i in range(max_left):
        # Move left
        _ = _ >> 1
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    return moves


def get_white_rook_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white rook starting at position can reach
    """
    return get_rook_moves(board, "white", position)


def get_black_rook_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a black rook starting at position can reach
    """
    return get_rook_moves(board, "black", position)


def get_bishop_moves(board, side: str, position: int) -> list[int]:
    """
    Returns a list of end positions a bishop of side=side can reach starting at position
    """
    moves = []
    file = get_file(position)
    max_right = 8 - file
    _ = position
    for i in range(max_right):
        _ = _ << 9
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    _ = position
    for i in range(max_right):
        _ = _ >> 7
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    max_left = file - 1
    _ = position
    for i in range(max_left):
        _ = _ << 7
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    _ = position
    for i in range(max_left):
        _ = _ >> 9
        valid, should_break = check_valid_position(board, side, position, _, moves)
        if should_break:
            break

    return moves


def get_white_bishop_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white bishop starting at position can reach
    """
    return get_bishop_moves(board, "white", position)


def get_black_bishop_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a black bishop starting at position can reach
    """
    return get_bishop_moves(board, "black", position)


def get_knight_moves(board, side: str, position: int) -> list[int]:
    """
    Returns a list of end positions a knight starting at position can reach
    """
    moves = []
    rank = get_rank(position)
    file = get_file(position)

    if rank >= 3:
        if file >= 2:
            _ = position >> 17
            check_valid_position(board, side, position, _, moves)
        if file <= 7:
            _ = position >> 15
            check_valid_position(board, side, position, _, moves)

    if rank >= 2:
        if file >= 3:
            _ = position >> 10
            check_valid_position(board, side, position, _, moves)
        if file <= 6:
            _ = position >> 6
            check_valid_position(board, side, position, _, moves)

    if rank <= 6:
        if file >= 2:
            _ = position << 15
            check_valid_position(board, side, position, _, moves)
        if file <= 7:
            _ = position << 17
            check_valid_position(board, side, position, _, moves)

    if rank <= 7:
        if file >= 3:
            _ = position << 6
            check_valid_position(board, side, position, _, moves)
        if file <= 6:
            _ = position << 10
            check_valid_position(board, side, position, _, moves)

    return moves


def get_white_knight_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white knight starting at position can reach
    """
    return get_knight_moves(board, "white", position)


def get_black_knight_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a black knight starting at position can reach
    """
    return get_knight_moves(board, "black", position)


def get_king_moves(board, side: str, position: int) -> list[int]:
    """
    Returns a list of end positions a king starting at position can reach
    """
    moves = []

    rank = get_rank(position)
    file = get_file(position)

    if rank >= 2:
        _ = position >> 8
        check_valid_position(board, side, position, _, moves)

        if file >= 2:
            _ = position >> 9
            check_valid_position(board, side, position, _, moves)

        if file <= 7:
            _ = position >> 7
            check_valid_position(board, side, position, _, moves)

    if rank <= 7:
        _ = position << 8
        check_valid_position(board, side, position, _, moves)

        if file >= 2:
            _ = position << 7
            check_valid_position(board, side, position, _, moves)

        if file <= 7:
            _ = position << 9
            check_valid_position(board, side, position, _, moves)

    if file >= 2:
        _ = position >> 1
        check_valid_position(board, side, position, _, moves)

    if file <= 7:
        _ = position << 1
        check_valid_position(board, side, position, _, moves)
    return moves


def get_white_king_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white king starting at position can reach
    """
    return get_king_moves(board, "white", position)


def get_black_king_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a black king starting at position can reach
    """
    return get_king_moves(board, "black", position)


def get_white_queen_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a white queen starting at position can reach
    """
    return get_white_rook_moves(board, position) + get_white_bishop_moves(
        board, position
    )


def get_black_queen_moves(board, position: int) -> list[int]:
    """
    Returns a list of end positions a black queen starting at position can reach
    """
    return get_black_rook_moves(board, position) + get_black_bishop_moves(
        board, position
    )


def get_white_pawn_moves(
    board, position: int, allow_en_passant: bool = False
) -> list[tuple[int, int]]:
    """
    Returns a list of end positions a white pawn starting at position can reach
    """
    rank = get_rank(position)
    if rank == 8:
        return []

    moves = []
    _ = position << 8
    if board.all_pieces & _ == 0:
        moves.append((position, _))
        if rank == 2:
            _ = position << 16
            if board.all_pieces & _ == 0:
                moves.append((position, _))
    file = get_file(position)
    if file >= 2:
        _ = position << 7
        if board.all_black & _ > 0:
            moves.append((position, _))
    if file <= 7:
        _ = position << 9
        if board.all_black & _ > 0:
            moves.append((position, _))

    if allow_en_passant:
        if file >= 2:
            _ = position << 7
            check_valid_position(board, "white", position, _, moves)
        if file <= 7:
            _ = position << 9
            check_valid_position(board, "white", position, _, moves)

    return moves


def get_black_pawn_moves(
    board, position: int, allow_en_passant: bool = False
) -> list[tuple[int, int]]:
    """
    Returns a list of end positions a black pawn starting at position can reach
    """
    rank = get_rank(position)
    if rank == 1:
        return []

    moves = []
    _ = position >> 8
    if board.all_pieces & _ == 0:
        moves.append((position, _))
        if rank == 7:
            _ = position >> 16
            if board.all_pieces & _ == 0:
                moves.append((position, _))
    file = get_file(position)
    if file >= 2:
        _ = position >> 9
        if board.all_white & _ > 0:
            moves.append((position, _))
    if file <= 7:
        _ = position >> 7
        if board.all_white & _ > 0:
            moves.append((position, _))

    if allow_en_passant:
        if file >= 2:
            _ = position >> 9
            check_valid_position(board, "black", position, _, moves)
        if file <= 7:
            _ = position >> 7
            check_valid_position(board, "black", position, _, moves)

    return moves
