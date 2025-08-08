"""
在 Python 中，ord() 函数用于获取单个字符的 Unicode 码点（整数表示）。当你将 ord() 转换后的值再转换为字符串时，实际上只是将这个整数转为它的字符串形式。
在 Unicode 标准中，每个字符的码点（Code Point）是唯一的
"""
a = 'asasd'
print(ord(a[1]))