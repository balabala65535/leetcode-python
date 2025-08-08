from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        按层模拟
        """
        if not matrix and not matrix[0]:
            return []
        rows = len(matrix)
        columns = len(matrix[0])
        left, right, top, bottom = 0, columns - 1, 0, rows - 1

        res = []
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])

            # 判断要不要逆拐弯
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    res.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom -1
        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        turn = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []

        rows = len(matrix)
        columns = len(matrix[0])
        scaned = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total
        row, colum = 0, 0
        turn_index = 0
        for i in range(total):
            order[i] = matrix[row][colum]
            scaned[row][colum] = True
            nextRow, nextColum = row + turn[turn_index][0], colum + turn[turn_index][1]
            if not (0 <= nextRow < rows and 0 <= nextColum < columns and not scaned[nextRow][nextColum]):
                turn_index = (turn_index + 1) % 4
            row, colum = row + turn[turn_index][0], colum + turn[turn_index][1]
        return order


def spiralOrder(matrix):
    """
    模拟: 1%&24%
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix or not matrix[0]:
        return list()

    rows, columns = len(matrix), len(matrix[0])
    visited = [[False] * columns for _ in range(rows)]
    total = rows * columns
    order = [0] * total

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    row, column = 0, 0
    directionIndex = 0
    for i in range(total):
        order[i] = matrix[row][column]
        visited[row][column] = True
        nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
        print(nextRow, nextColumn)
        print(visited)
        # print(visited[nextRow][nextColumn])
        # 判定何时转弯？？nextRow 超过了row,nextColumn 超过了columns, nextRow&nextColumn都有被visited
        if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
            # 判断要不要转弯
            # 1.将要看的行和列超出了限制
            # 2.当前元素已经被看过了
            directionIndex = (directionIndex + 1) % 4  # 为什么是4？
            print(f"new directionIndex:{directionIndex}")
        row += directions[directionIndex][0]
        column += directions[directionIndex][1]
    return order


def spiralOrder_1(matrix):
    """
    按层模拟: 100%&80%
    :param matrix:
    :return:
    """
    if not matrix or not matrix[0]:
        return list()

    rows, columns = len(matrix), len(matrix[0])
    order = list()
    left, right, top, bottom = 0, columns - 1, 0, rows - 1
    while left <= right and top <= bottom:
        for column in range(left, right + 1):
            order.append(matrix[top][column])
        for row in range(top + 1, bottom + 1):
            order.append(matrix[row][right])
        if left < right and top < bottom:  # 还有多块待扫描的区域
            for column in range(right - 1, left, -1):
                order.append(matrix[bottom][column])
            for row in range(bottom, top, -1):
                order.append(matrix[row][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return order


def spiralOrder_2(matrix):
    """
    100%&12%
    用向量变换的公式代替了原始的4个方向向量。
    """
    m, n = len(matrix), len(matrix[0])
    x, y, dx, dy = 0, 0, 0, 1
    res = []
    for _ in range(m*n):
        res.append(matrix[x][y])
        matrix[x][y] = '.'

        if not 0 <= x+dx < m or not 0 <= y+dy < n or matrix[x+dx][y+dy] == '.':
            dx, dy = dy, -dx
        x += dx
        y += dy
    return res



def spiralOrder_3(matrix):
    """
    100%&18%
    :param matrix:
    :return:
    """
    res = []
    l = 0
    r = len(matrix[0]) -1
    u = 0
    d = len(matrix) -1

    while u <= d and l <= r:

        # 从左到右
        j = l
        while u <= d and j <= r:
            res.append(matrix[u][j])
            j += 1
        u += 1  # 扫完一行了，所以u从0变为了1

        # 从上到下
        i = u
        while l <= r and i <= d:
            res.append(matrix[i][r])
            i += 1
        r -= 1  # 扫完一列，所以r就少了一列

        # 从右到左
        j = r
        while u <= d and j >= l:
            res.append(matrix[d][j])
            j -= 1
        d -= 1  # 扫完最下面一排，所以减少一行

        # 从下到上
        i = d
        while l <= r and i >= u:
            res.append(matrix[i][l])
            i -= 1
        l += 1  # 扫完了最右列

    return res


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    resp = spiralOrder_3(matrix)
    print(resp)