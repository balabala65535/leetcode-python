# Python 中类似 `collections` 的实用模块工具

除了 `collections` 模块外，Python 标准库还提供了许多其他实用的容器和数据结构模块。以下是几个值得关注的类似工具：

## 1. `array` 模块
**用途**：高效存储同类型数据（类似C语言的数组）

```python
import array

# 创建一个整数数组
int_array = array.array('i', [1, 2, 3, 4, 5])  # 'i'表示有符号整数
print(int_array)  # array('i', [1, 2, 3, 4, 5])

# 比列表更节省内存
float_array = array.array('f', [1.0, 2.5, 3.7])
float_array.append(4.2)  # 支持类似列表的操作
```

## 2. `heapq` 模块
**用途**：堆队列算法（优先队列实现）

```python
import heapq

# 创建最小堆
nums = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(nums)
print(nums)  # [1, 1, 2, 3, 5, 9, 4]

# 堆操作
heapq.heappush(nums, 0)
print(heapq.heappop(nums))  # 0
```

## 3. `bisect` 模块
**用途**：维护有序列表的插入和查找

```python
import bisect

sorted_list = [1, 3, 5, 7, 9]
bisect.insort(sorted_list, 4)  # 保持有序插入
print(sorted_list)  # [1, 3, 4, 5, 7, 9]

# 查找插入位置
print(bisect.bisect_left(sorted_list, 6))  # 4 (插入位置索引)
```

## 4. `queue` 模块
**用途**：线程安全的队列实现

```python
from queue import Queue, LifoQueue, PriorityQueue

# 先进先出队列
q = Queue(maxsize=3)
q.put('a')
q.put('b')
print(q.get())  # 'a'

# 后进先出栈
stack = LifoQueue()
stack.put(1)
stack.put(2)
print(stack.get())  # 2

# 优先级队列
pq = PriorityQueue()
pq.put((3, 'low'))
pq.put((1, 'high'))
print(pq.get()[1])  # 'high'
```

## 5. `weakref` 模块
**用途**：实现弱引用（不影响垃圾回收）

```python
import weakref

class MyClass:
    pass

obj = MyClass()
weak_obj = weakref.ref(obj)  # 创建弱引用

print(weak_obj())  # <__main__.MyClass object at ...>
del obj
print(weak_obj())  # None (原对象被回收)
```

## 6. `enum` 模块
**用途**：创建枚举类型

```python
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)        # Color.RED
print(Color.RED.value)  # 1

# 自动赋值
class AutoColor(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
```

## 7. `dataclasses` 模块 (Python 3.7+)
**用途**：自动生成样板代码的数据类

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # 默认值

p = Point(1.5, 2.5)
print(p)  # Point(x=1.5, y=2.5, z=0.0)
```

## 8. `functools` 模块
**用途**：高阶函数和可调用对象操作

```python
from functools import lru_cache, partial

# 缓存装饰器
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 部分函数应用
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```

## 9. `itertools` 模块
**用途**：高效循环迭代器工具

```python
import itertools

# 无限迭代器
counter = itertools.count(start=10, step=2)
print(next(counter), next(counter))  # 10, 12

# 组合迭代器
print(list(itertools.permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

## 10. `contextlib` 模块
**用途**：上下文管理器工具

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("获取资源")
    yield "资源对象"
    print("释放资源")

with managed_resource() as r:
    print(f"使用 {r}")
```

这些模块与 `collections` 类似，都是 Python 标准库中提供的实用工具模块，每个模块都专注于解决特定类型的问题。根据不同的需求选择合适的模块可以大大提高开发效率和代码质量。