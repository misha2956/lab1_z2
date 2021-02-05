"""
Github: https://github.com/misha2956/lab1_z2

This module is created to validate a board
"""

from itertools import chain

def check_numbers_unique(number_list: list) -> bool:
    """
    Checks whether numbers in list are all unique

    >>> check_numbers_unique([1, 2, 3])
    True
    >>> check_numbers_unique([1, 2, 2])
    False
    """

    number_set = set()

    for number in number_list:
        if number not in number_set:
            number_set.add(number)
        else:
            return False

    return True


def all_rows_generator(board: list):
    """
    This function is a generator for all rows of a board

    >>> [a for a in all_rows_generator(["ab", "*d"])]
    [['a', 'b'], ['d']]
    """

    for i, _ in enumerate(board):
        yield [
            board[i][j]
            for j, _ in enumerate(board[i])
            if board[i][j] not in ['*', ' ']
        ]


def all_cols_generator(board: list):
    """
    This function is a generator for all cols of a board

    >>> [a for a in all_cols_generator(["ab", "*d"])]
    [['a'], ['b', 'd']]
    """

    return (
        [
            board[i][j]
            for i, _ in enumerate(board)
            if board[i][j] not in ['*', ' ']
        ] for j, _ in enumerate(board[0])
    )


def all_angles_generator(board: list):
    """
    This function is a generator for all angles of a board

    >>> board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"]
    >>> [a for a in all_angles_generator(board)][0]
    ['3', '1', '9', '5']
    """

    def angle(start_i, start_j, board):
        return [
            board[i][start_j]
            for i in range(start_i, start_i + 5)
            if board[i][start_j] not in ['*', ' ']
        ] + [
            board[start_i + 4][j]
            for j in range(start_j, start_j + 5)
            if board[start_i + 4][j] not in ['*', ' ']
        ]

    for start_j, start_i in zip(range(4, -1, -1), range(5)):
        yield angle(start_i, start_j, board)


def validate_board(board: list) -> bool:
    """
    This function validates a board.

    >>> board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"]
    >>> validate_board(board)
    False
    """

    for number_list in chain(
            (line for line in board),
            all_cols_generator, all_angles_generator
    ):
        if not check_numbers_unique(number_list):
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
