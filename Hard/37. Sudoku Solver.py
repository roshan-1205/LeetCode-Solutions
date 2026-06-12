"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells."""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    d = board[r][c]
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[(r // 3) * 3 + c // 3].add(d)

        def backtrack(i):
            if i == len(empty):
                return True
            r, c = empty[i]
            box = (r // 3) * 3 + c // 3
            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[box]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[box].add(d)
                    if backtrack(i + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].discard(d)
                    cols[c].discard(d)
                    boxes[box].discard(d)
            return False

        backtrack(0)