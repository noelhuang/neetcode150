import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rowdict = collections.defaultdict(set)  # every key is a row
        coldict = collections.defaultdict(set)  # every key is a column

        fielddict = collections.defaultdict(set)  # every key is a tuple (row, column) coordinates

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] == ".":
                    continue
                fieldrow = i // 3
                fieldcol = j // 3
                if board[i][j] in rowdict[i] or board[i][j] in coldict[j] or board[i][j] in fielddict[(fieldrow, fieldcol)]:
                    return False
                rowdict[i].add(board[i][j])
                coldict[j].add(board[i][j])
                fielddict[(fieldrow, fieldcol)].add(board[i][j])
        return True