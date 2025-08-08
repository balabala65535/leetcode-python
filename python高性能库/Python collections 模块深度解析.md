# Python `collections` 模块深度解析

`collections` 是 Python 标准库中一个非常实用的模块，提供了许多有用的容器数据类型，作为内置容器（如 `dict`, `list`, `set`, `tuple`）的替代和扩展。

## 1. Counter（计数器）

**用途**：用于统计可哈希对象的出现次数

```python
from collections import Counter

# 创建计数器
cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(cnt)  # Counter({'a': 3, 'b': 2, 'c': 1})

# 常用操作
print(cnt.most_common(2))  # [('a', 3), ('b', 2)]
print(cnt['a'])  # 3
print(cnt['d'])  # 0 (不存在的元素返回0)

# 更新计数器
cnt.update(['a', 'b', 'd'])
print(cnt)  # Counter({'a': 4, 'b': 3, 'c': 1, 'd': 1})

# 数学运算
cnt2 = Counter('abracadabra')
print(cnt + cnt2)  # 合并计数
print(cnt - cnt2)  # 减法（只保留正数计数）
```

## 2. defaultdict（默认字典）

**用途**：为字典提供默认值，避免 KeyError

```python
from collections import defaultdict

# 创建默认字典
dd = defaultdict(int)  # 默认值为0
dd['a'] += 1
print(dd['b'])  # 0 (自动创建)

# 使用list作为默认值
dd_list = defaultdict(list)
dd_list['colors'].append('red')
print(dd_list)  # defaultdict(<class 'list'>, {'colors': ['red']})

# 使用自定义函数
def default_value():
    return 'unknown'
    
dd_custom = defaultdict(default_value)
print(dd_custom['name'])  # 'unknown'
```

## 3. OrderedDict（有序字典）

**用途**：保持元素插入顺序（Python 3.7+ 普通 dict 也已有序）

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(list(od.keys()))  # ['a', 'b', 'c']

# 特殊方法
od.move_to_end('a')  # 将键移动到末尾
print(list(od.keys()))  # ['b', 'c', 'a']

od.popitem(last=False)  # FIFO顺序弹出
print(od)  # OrderedDict([('c', 3), ('a', 1)])
```

## 4. deque（双端队列）

**用途**：高效实现队列和栈操作

```python
from collections import deque

d = deque('ghi')  # 创建双端队列
d.append('j')     # 右侧添加
d.appendleft('f') # 左侧添加
print(d)          # deque(['f', 'g', 'h', 'i', 'j'])

d.pop()           # 右侧弹出
d.popleft()       # 左侧弹出
print(d)          # deque(['g', 'h', 'i'])

# 其他操作
d.rotate(1)       # 向右旋转1位
print(d)          # deque(['i', 'g', 'h'])

d.extendleft('ab') # 左侧扩展
print(d)          # deque(['b', 'a', 'i', 'g', 'h'])
```

## 5. namedtuple（命名元组）

**用途**：创建具有字段名的轻量级类

```python
from collections import namedtuple

# 创建命名元组类型
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)  # 创建实例

print(p.x, p.y)      # 11 22
print(p[0], p[1])    # 11 22 (仍支持索引)

# 转换为字典
print(p._asdict())   # {'x': 11, 'y': 22}

# 替换字段值
new_p = p._replace(x=33)
print(new_p)         # Point(x=33, y=22)
```

## 6. ChainMap（链式映射）

**用途**：将多个字典链接为一个视图

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)
print(cm['a'])  # 1 (来自dict1)
print(cm['b'])  # 2 (来自dict1，优先使用第一个字典的值)
print(cm['c'])  # 4 (来自dict2)

# 更新操作只影响第一个字典
cm['c'] = 5
print(dict2)  # {'b': 3, 'c': 4} (未改变)
print(dict1)  # {'a': 1, 'b': 2, 'c': 5}

# 添加新字典
cm = cm.new_child({'d': 6})
print(cm['d'])  # 6
```

## 7. UserDict/UserList/UserString（包装类）

**用途**：创建自定义字典/列表/字符串类的基类

```python
from collections import UserDict

class MyDict(UserDict):
    def __missing__(self, key):
        return f'[{key} not found]'
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

md = MyDict({'a': 1})
print(md['a'])  # 2 (值被加倍)
print(md['b'])  # [b not found] (处理缺失键)
```

## 实际应用场景

1. **Counter**：词频统计、数据分析
2. **defaultdict**：构建复杂数据结构如树、图
3. **deque**：实现队列、栈、滑动窗口算法
4. **namedtuple**：替代简单类，提高代码可读性
5. **OrderedDict**：需要保持顺序的缓存实现
6. **ChainMap**：配置优先级管理、变量作用域模拟

`collections` 模块的这些工具可以显著提高代码的简洁性和效率，是Python程序员的重要工具包。