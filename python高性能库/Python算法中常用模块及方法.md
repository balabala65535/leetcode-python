# Python算法中常用模块及方法

Python标准库提供了许多强大的模块，可以显著简化算法实现。以下是算法设计和实现中最常用的模块及其关键方法：

## 1. 数据结构相关模块

### `collections` 模块
```python
from collections import deque, defaultdict, Counter, OrderedDict

# 双端队列
dq = deque([1,2,3])
dq.appendleft(0)  # 左端添加
dq.pop()          # 右端弹出

# 默认字典
dd = defaultdict(list)
dd['key'].append(1)

# 计数器
cnt = Counter('abracadabra')
cnt.most_common(3)  # 最常见的3个元素

# 有序字典
od = OrderedDict()
od['a'] = 1; od['b'] = 2
```

### `heapq` 模块 (堆/优先队列)
```python
import heapq

nums = [3,1,4,1,5,9]
heapq.heapify(nums)     # 转换为最小堆
heapq.heappush(nums, 2) # 压入元素
val = heapq.heappop(nums) # 弹出最小值

# 获取前n个最大/最小值
heapq.nlargest(3, nums)
heapq.nsmallest(2, nums)
```

### `bisect` 模块 (二分查找)
```python
import bisect

arr = [1,3,5,7]
bisect.insort(arr, 4)  # 保持有序插入
idx = bisect.bisect_left(arr, 5)  # 查找插入位置
```

## 2. 数学与数值计算

### `math` 模块
```python
import math

math.sqrt(16)       # 平方根
math.gcd(48, 18)    # 最大公约数
math.comb(5, 2)     # 组合数C(5,2)
math.perm(5, 2)     # 排列数P(5,2)
math.log(x, 2)      # 对数
math.factorial(5)   # 阶乘
```

### `random` 模块
```python
import random

random.random()        # [0,1)随机浮点数
random.randint(1,10)   # [1,10]随机整数
random.shuffle(lst)    # 列表随机排序
random.choice(lst)     # 随机选择元素
random.sample(lst, k)  # 无重复抽样
```

## 3. 迭代工具

### `itertools` 模块
```python
import itertools

# 组合迭代器
itertools.permutations('ABC', 2)  # 排列
itertools.combinations('ABC', 2)  # 组合
itertools.product('AB', repeat=2) # 笛卡尔积

# 无限迭代器
itertools.count(10, 2)  # 10,12,14...
itertools.cycle('AB')   # A,B,A,B...

# 分组
for key, group in itertools.groupby('AAABBBCC'):
    print(key, list(group))
```

## 4. 算法辅助工具

### `functools` 模块
```python
from functools import lru_cache, cmp_to_key

# 记忆化缓存
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# 自定义排序
sorted([5,3,7], key=cmp_to_key(custom_compare))
```

### `operator` 模块
```python
from operator import itemgetter, attrgetter

# 用于排序
sorted(lst, key=itemgetter(1))  # 按第二元素排序
sorted(objs, key=attrgetter('age'))  # 按属性排序
```

## 5. 字符串处理

### `re` 模块 (正则表达式)
```python
import re

re.findall(r'\d+', 'a1b22c')  # ['1', '22']
re.sub(r'\s+', '-', text)     # 替换空格
pattern = re.compile(r'[A-Z]+')
pattern.findall('ABCdefGHI')  # ['ABC', 'GHI']
```

### `string` 模块
```python
import string

string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
string.digits           # '0123456789'
string.punctuation      # 所有标点符号
```

## 6. 系统与性能

### `sys` 模块
```python
import sys

sys.setrecursionlimit(10000)  # 设置递归深度
sys.getsizeof(obj)           # 获取对象内存大小
```

### `timeit` 模块 (性能测试)
```python
import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
```

## 7. 图算法辅助

### 优先队列实现 (Dijkstra算法等)
```python
import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0  # 处理相同优先级
    
    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._heap)[-1]
```

## 实际算法应用示例

### 拓扑排序 (使用defaultdict和deque)
```python
from collections import deque, defaultdict

def topological_sort(graph):
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in graph if in_degree[u] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return result if len(result) == len(graph) else None
```

这些模块和方法构成了Python算法实现的基础工具包，熟练掌握它们可以大大提高算法实现的效率和质量。