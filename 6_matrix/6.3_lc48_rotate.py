


def rotate(matrix):
    """
    使用辅助数组： 100%&5%
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    import copy
    org_matrix = copy.deepcopy(matrix)
    m = len(matrix)
    for i in range(m):
        for j in range(m):
            matrix[j][m-1-i] = org_matrix[i][j]


def rotate_1(matrix):
    """
    翻转
    :param matrix:
    :return:
    """
    n = len(matrix)
    # 水平翻转
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    # 主对角线翻转
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]





def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


def rotate_4(matrix):
    """
    7%&14%
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    import copy
    org_matrix = copy.deepcopy(matrix)
    m = len(matrix)
    for i in range(m):
        for j in range(m):
            matrix[j][m-1-i] = org_matrix[i][j]
            matrix[i][j] = org_matrix[m - j - 1][i]

def rotate_5(matrix):
    """
    7%&14%
    拆分顺序：[[7, 4, 7], [6, 5, 6], [9, 6, 9]]
    未拆分顺序：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = m = len(matrix)
    for i in range(m//2):
        for j in range((m + 1)//2):
            # matrix[i][j] = matrix[m - j - 1][i]
            # matrix[m - j - 1][i] = matrix[m - i - 1][m - j - 1]
            # matrix[m - i - 1][m - j - 1] = matrix[j][m - i - 1]
            # matrix[j][m - 1 - i] = matrix[i][j]
            matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate_5(matrix)
    print(matrix)