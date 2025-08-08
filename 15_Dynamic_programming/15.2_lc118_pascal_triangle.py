


def generate_pascal_triangle(n: int) -> list[list[int]]:
    """迭代法
    """
    triangle = []
    for row_num in range(n):
        row = [1]  # 每行第一个元素是1
        if triangle:  # 如果不是第一行
            last_row = triangle[-1]
            row.extend([last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)])
            row.append(1)  # 每行最后一个元素是1
        triangle.append(row)
    return triangle

# 测试
n = 5
triangle = generate_pascal_triangle(n)
for row in triangle:
    print(row)


from math import comb  # Python 3.10+

def generate_pascal_triangle_math(n: int) -> list[list[int]]:
    return [[comb(row, k) for k in range(row + 1)] for row in range(n)]

# 测试
n = 5
triangle = generate_pascal_triangle_math(n)
for row in triangle:
    print(row)

def pascal_triangle_recursive(n: int) -> list[list[int]]:
    """
    递归实现（不推荐，效率低）
    :param n:
    :return:
    """
    if n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle_recursive(n - 1)
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)
        return triangle

# 测试
n = 5
triangle = pascal_triangle_recursive(n)
for row in triangle:
    print(row)


def generate_pascal_triangle_dp(n: int) -> list[list[int]]:
    """动态规划优化
    推荐使用迭代法或动态规划，它们效率高且代码简洁！
    """
    triangle = [[1] * (i + 1) for i in range(n)]  # 初始化全1三角形
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

# 测试
n = 5
triangle = generate_pascal_triangle_dp(n)
for row in triangle:
    print(row)