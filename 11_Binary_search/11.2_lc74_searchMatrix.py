
import bisect


def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    # 找到第一个matrix[i][0] > target的行，然后减1得到可能所在的行
    row = bisect.bisect_right([row[0] for row in matrix], target) - 1
    if row < 0:
        return False

    # 在该行中二分查找target
    col = bisect.bisect_left(matrix[row], target)
    return col < len(matrix[row]) and matrix[row][col] == target


if __name__ == "__main__":
    matrix = [[1,3,5,7],[2,11,16,20],[23,30,34,60]]
    target = 3
    res = bisect.bisect_right([row[0] for row in matrix], target)
    print(res)
