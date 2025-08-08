
def searchMatrix(matrix, target):
    """
    74%&37% 优化后60%&89%
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    matched = False
    for i in matrix:
        if target in i:
            matched = True
        if i[0] > target:
            break
    return matched


def searchMatrix_1(matrix, target):
    """二分查找
    99% & 88%
    """
    import bisect
    for row in matrix:
        idx = bisect.bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True


def searchMatrix_3(matrix, target):
    """
    方法 1：利用矩阵的单调性（二分搜索）
    假设矩阵的每一行按升序排列，且每行的首元素大于前一行的末尾元素（即整个矩阵是全局有序的）：
    时间复杂度：O(log(m*n))（二分搜索）。
    空间复杂度：O(1)。
    :param matrix:
    :param target:
    :return:
    """
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // n][mid % n]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def searchMatrix_4(matrix, target):
    """
    方法三：Z 字形查找
    70% & 15%
    :param matrix:
    :param target:
    :return:
    """
    m, n = len(matrix), len(matrix[0])
    x, y = 0, n - 1
    while x < m and y >= 0:
        if matrix[x][y] == target:
            return True
        if matrix[x][y] > target:
            y -= 1
        else:
            x += 1
    return False
