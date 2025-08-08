def setZeroes(matrix):
    """
    6%&24%，优化后6%&8.95%
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    find_x_zorro = []
    find_y_zorro = []
    for x, h in enumerate(matrix):
        for y, v in enumerate(h):
            if v == 0:
                find_x_zorro.append(x)
                find_y_zorro.append(y)
    # 设置0
    for x, h in enumerate(matrix):
        for y, v in enumerate(h):
            if x in find_x_zorro or y in find_y_zorro:
                matrix[x][y] = 0
    return matrix


def setZeroes_1(matrix):
    """
    5% & 70%
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    # 设置0
    for x, h in enumerate(matrix):
        if 0 in h:
            # 找到x 的y轴
            matrix[x] = [i if i == 0 else None for i in h]
            for y in range(n):
                if h[y] == 0:
                    for i in range(m):
                        if i == x:
                            continue
                        if matrix[i][y] != 0:
                            matrix[i][y] = None
    # 将None 变为0
    for x, h in enumerate(matrix):
        for y, v in enumerate(h):
            if v is None:
                matrix[x][y] = 0
    return matrix


def setZeroes_2(matrix):
    """
    10%&52%
    :param matrix:
    :return:
    """
    m = len(matrix)
    n = len(matrix[0])
    # 设置0
    for x, h in enumerate(matrix):
        if 0 in h:
            # 找到x 的y轴
            matrix[x] = [i if i == 0 else None for i in h]

    for y in range(n):
        x_y = [matrix[i][y] for i in range(m)]
        if 0 in x_y:
            for x in range(m):
                matrix[x][y] = None if matrix[x][y] != 0 else 0

    # 将None 变为0
    for x, h in enumerate(matrix):
        for y, v in enumerate(h):
            if v is None:
                matrix[x][y] = 0
    return matrix


def setZeroes_3(matrix):
    """
    官方：使用标记数组。 49%&70%
    :param matrix:
    :return:
    """
    m = len(matrix)
    n = len(matrix[0])
    row, column = [False] * m, [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = column[j] = True
    print(row)
    print(column)
    for i in range(m):
        for j in range(n):
            if row[i] or column[j]:
                matrix[i][j] = 0


def setZeroes_4(matrix):
    """
    官方：使用两个标记变量,
    """
    m, n = len(matrix), len(matrix[0])
    flag_col0 = any(matrix[i][0] == 0 for i in range(m))
    flag_row0 = any(matrix[0][j] == 0 for j in range(n))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if flag_col0:
        for i in range(m):
            matrix[i][0] = 0

    if flag_row0:
        for j in range(n):
            matrix[0][j] = 0


def setZeroes_5(matrix):
    m, n = len(matrix), len(matrix[0])
    flag_col0 = False

    for i in range(m):
        if matrix[i][0] == 0:
            flag_col0 = True
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(m - 1, -1, -1):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if flag_col0:
            matrix[i][0] = 0


if __name__ == "__main__":
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    resp = setZeroes_5(matrix)
    print(resp)
    print(matrix)
