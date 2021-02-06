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
            if number not in [' ', '*']:
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
    [['a', '*'], ['b', 'd']]
    """

    return (
        [
            board[i][j]
            for i, _ in enumerate(board)
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
    [' ', ' ', '3', '1', ' ', '9', ' ', '5', ' ']
    """

    def angle(start_i, start_j, board):
        return [
            board[i][start_j]
            for i in range(start_i, start_i + 5)
        ] + [
            board[start_i + 4][j]
            for j in range(start_j + 1, start_j + 5)
        ]

    for start_j, start_i in zip(range(4, -1, -1), range(5)):
        yield angle(start_i, start_j, board)


def replace_with_white(board: list):
    """
    Replaces white boxes with '*'

    >>> board = [\
    "*1** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"]
    >>> replace_with_white(board)[0]
    '**** ****'
    """

    for i in range(4):
        j = 4 - i
        board[i] = "*" * j + board[i][j:-4] + 4 * '*'

    for i in range(-1, -5, -1):
        j = -4 + (abs(i) - 1)
        board[i] = board[i][:j] + "*" * abs(j)

    return board


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
    >>> board = [\
    "**** ****",\
    "1**1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   2  **",\
    "  8  2***",\
    "  2  ****"]
    >>> validate_board(board)
    True
    >>> board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   2  **",\
    "  8  2***",\
    "  2  ****"]
    >>> validate_board(board)
    True
    >>> board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     1 5 ",\
    " 6  83  *",\
    "3   2  **",\
    "  8  2***",\
    "  2  ****"]
    >>> validate_board(board)
    False
    >>> board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 9 ",\
    " 6  83  *",\
    "3   2  **",\
    "  8  2***",\
    "  2  ****"]
    >>> validate_board(board)
    False
    """

    board = replace_with_white(board)

    for number_list in chain(
            (line for line in board),
            all_cols_generator(board), all_angles_generator(board)
    ):
        # print(number_list)
        if not check_numbers_unique(number_list):
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
