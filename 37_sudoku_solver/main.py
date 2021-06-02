from typing import List
import numpy as np


class Solution:
    solvedBoard = []

    def solveSudoku(self, board: List[List[str]]) -> None:
        self._solveSudokuHelper(board)
        for i in range(9):
            board[i] = self.solvedBoard[i]

    def _solveSudokuHelper(self, board: List[List[str]]) -> None:
        # print(board[:2])
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for n in range(9):
                        if self._canPlace(board, r, c, str(n + 1)):
                            # print(n)
                            board[r][c] = str(n + 1)
                            self._solveSudokuHelper(board)
                            board[r][c] = "."

                    return

        for i in range(9):
            # print(i, board[i])
            self.solvedBoard.append(board[i].copy())

        return

    def _canPlace(self, board, row, col, n) -> bool:
        for k in range(9):
            if board[row][k] == n:
                return False

            if board[k][col] == n:
                return False

        boxCornerRow = row // 3 * 3
        boxCornerCol = col // 3 * 3

        for i in range(3):
            for j in range(3):
                if board[boxCornerRow + i][boxCornerCol + j] == n:
                    return False

        return True


if __name__ == '__main__':
    test_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol = Solution()

    sol.solveSudoku(test_board)
    print(np.array(test_board))

    test_board = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."],
    ]
