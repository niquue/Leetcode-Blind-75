"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1



Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

"""


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    def helper(i, j):
        row, col = i, j
        while col > -1:
            if matrix[i][col] != 0:
                matrix[i][col] = True
                col -= 1
            elif matrix[i][col] == 0:
                col -= 1
        row, col = i, j
        while col < len(matrix[i]):
            if matrix[i][col] != 0:
                matrix[i][col] = True
                col += 1
            elif matrix[i][col] == 0:
                col += 1
        row, col = i, j
        while row > -1:
            if matrix[row][j] != 0:
                matrix[row][j] = True
                row -= 1
            elif matrix[row][j] == 0:
                row -= 1
        row, col = i, j
        while row < len(matrix):
            if matrix[row][j] != 0:
                matrix[row][j] = True
                row += 1
            elif matrix[row][j] == 0:
                row += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                helper(i, j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] is True:
                matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)