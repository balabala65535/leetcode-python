# **Python `collections` 模块详解**

`collections` 是 Python 标准库中的一个模块，提供了许多**高性能、专用的容器数据类型**，用于替代 Python 内置的通用容器（如 `list`、`dict`、`tuple` 等）。这些数据结构在特定场景下能显著提升代码效率和可读性。

---

## **1. `collections` 模块的核心数据结构**
以下是 `collections` 中最常用的 5 个类：

| 类名 | 用途 | 替代的内置类型 |
|------|------|--------------|
| `defaultdict` | 带默认值的字典 | `dict` |
| `Counter` | 计数器（统计频率） | `dict` + 手动计数 |
| `deque` | 双端队列（高效插入/删除） | `list` |
| `namedtuple` | 命名元组（增强版 `tuple`） | `tuple` |
| `OrderedDict` | 有序字典（Python 3.7+ 普通 `dict` 已有序） | `dict` |

---

## **2. 详细功能介绍**

### **(1) `defaultdict`：带默认值的字典**
- **作用**：当访问不存在的键时，自动初始化默认值（避免 `KeyError`）。
- **典型用途**：统计词频、分组数据。

```python
from collections import defaultdict

# 示例1：统计单词频率
words = ["apple", "banana", "apple", "orange"]
word_count = defaultdict(int)  # 默认值 0
for word in words:
    word_count[word] += 1
print(word_count)  # 输出: defaultdict(<class 'int'>, {'apple': 2, 'banana': 1, 'orange': 1})

# 示例2：分组数据（比 setdefault 更高效）
anagrams = defaultdict(list)
for word in ["eat", "tea", "tan"]:
    key = ''.join(sorted(word))
    anagrams[key].append(word)
print(anagrams)  # 输出: defaultdict(<class 'list'>, {'aet': ['eat', 'tea'], 'ant': ['tan']})
```

---

### **(2) `Counter`：计数器**
- **作用**：快速统计可迭代对象中元素的频率。
- **典型用途**：统计词频、找Top N元素。

```python
from collections import Counter

# 示例1：统计字符频率
count = Counter("abracadabra")
print(count)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 示例2：找出现次数最多的2个元素
print(count.most_common(2))  # [('a', 5), ('b', 2)]

# 示例3：合并计数器
count2 = Counter("hello")
print(count + count2)  # Counter({'a': 5, 'b': 3, 'r': 2, 'l': 2, 'h': 1, 'e': 1, 'c': 1, 'd': 1, 'o': 1})
```

---

### **(3) `deque`：双端队列**
- **作用**：高效实现队列（FIFO）和栈（LIFO），支持两端快速插入/删除。
- **典型用途**：BFS算法、滑动窗口、历史记录。

```python
from collections import deque

# 示例1：队列操作（比 list.pop(0) 快）
q = deque([1, 2, 3])
q.append(4)    # 右端插入
q.popleft()    # 左端删除（输出: 1）

# 示例2：栈操作
stack = deque()
stack.append(1)  # 压栈
stack.pop()      # 弹栈（输出: 1）

# 示例3：固定长度队列（自动丢弃旧数据）
d = deque(maxlen=3)
d.extend([1, 2, 3])
d.append(4)  # 自动丢弃1
print(d)     # deque([2, 3, 4], maxlen=3)
```

---

### **(4) `namedtuple`：命名元组**
- **作用**：创建带有字段名的元组（类似轻量级类）。
- **典型用途**：替代简单类，提高代码可读性。

```python
from collections import namedtuple

# 定义命名元组
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)

# 访问字段
print(p.x, p.y)  # 1 2
print(p[0], p[1])  # 1 2（仍支持索引）

# 转换为字典
print(p._asdict())  # {'x': 1, 'y': 2}
```

---

### **(5) `OrderedDict`：有序字典**
- **作用**：保持键的插入顺序（Python 3.7+ 普通 `dict` 已有序，此类主要用于旧版本）。
- **典型用途**：需要保持顺序的字典操作。

```python
from collections import OrderedDict

d = OrderedDict()
d["a"] = 1
d["b"] = 2
print(d)  # OrderedDict([('a', 1), ('b', 2)])

# 最后插入的键移到末尾
d.move_to_end("a")
print(d)  # OrderedDict([('b', 2), ('a', 1)])
```

---

## **3. 其他实用工具**
- **`ChainMap`**：合并多个字典（逻辑合并，不创建新字典）。
- **`UserDict`/`UserList`/`UserString`**：方便自定义容器类。

```python
from collections import ChainMap

dict1 = {"a": 1}
dict2 = {"b": 2}
combined = ChainMap(dict1, dict2)
print(combined["a"])  # 1（优先访问 dict1）
```

---

## **4. 总结**
| 数据结构 | 核心优势 | 适用场景 |
|----------|---------|----------|
| `defaultdict` | 避免 `KeyError` | 分组、统计 |
| `Counter` | 快速计数 | 词频分析、Top N |
| `deque` | 高效两端操作 | 队列、栈、BFS |
| `namedtuple` | 字段名访问 | 替代简单类 |
| `OrderedDict` | 保持插入顺序 | 旧版本 Python 有序字典 |

**使用建议**：
- 需要统计频率 → `Counter`
- 需要分组数据 → `defaultdict`
- 需要高效队列/栈 → `deque`
- 需要更可读的元组 → `namedtuple`

`collections` 模块能显著提升代码性能和可读性，建议熟练掌握！ 🚀

---
# **队列（Queue）和栈（Stack）的区别**

队列和栈是两种常用的**线性数据结构**，它们在数据存取方式上有本质区别：

| 特性          | 队列 (Queue)               | 栈 (Stack)                |
|---------------|---------------------------|--------------------------|
| **数据存取规则** | **先进先出 (FIFO)**        | **后进先出 (LIFO)**       |
| **操作端**     | 两端操作（队尾入，队首出） | 单端操作（栈顶入，栈顶出） |
| **类比现实**   | 排队买票（先到先得）       | 叠盘子（最后放的先取）     |
| **典型用途**   | BFS算法、任务调度          | 函数调用、括号匹配         |
| **Python实现** | `collections.deque`        | 直接用 `list` 或 `deque`  |

---

## **1. 核心区别详解**
### **(1) 数据存取规则**
- **队列（FIFO）**  
  先进入的数据先被取出，就像排队买票：
  ```python
  from collections import deque
  q = deque()
  q.append(1)  # 队尾入队 -> [1]
  q.append(2)  # 队尾入队 -> [1, 2]
  q.popleft()  # 队首出队 -> 返回 1，剩余 [2]
  ```

- **栈（LIFO）**  
  后进入的数据先被取出，就像叠盘子：
  ```python
  stack = []
  stack.append(1)  # 入栈 -> [1]
  stack.append(2)  # 入栈 -> [1, 2]
  stack.pop()      # 出栈 -> 返回 2，剩余 [1]
  ```

---

### **(2) 操作端不同**
| 操作   | 队列                  | 栈                   |
|--------|-----------------------|----------------------|
| **插入** | `append()`（队尾）    | `append()`（栈顶）   |
| **删除** | `popleft()`（队首）   | `pop()`（栈顶）      |

> 📌 Python 中可以用 `deque` 实现队列和栈，但栈直接用 `list` 更简单。

---

### **(3) 可视化对比**
#### **队列（FIFO）**
```
输入顺序：A → B → C
输出顺序：A → B → C
```
```
队尾入队 → [C, B, A] → 队首出队
```

#### **栈（LIFO）**
```
输入顺序：A → B → C
输出顺序：C → B → A
```
```
栈顶入栈 → [A, B, C] → 栈顶出栈
```

---

## **2. 典型应用场景**
### **队列的用途**
1. **广度优先搜索（BFS）**  
   ```python
   from collections import deque
   def bfs(graph, start):
       visited, q = set(), deque([start])
       while q:
           node = q.popleft()
           for neighbor in graph[node]:
               if neighbor not in visited:
                   visited.add(neighbor)
                   q.append(neighbor)
   ```
2. **任务调度**（如打印任务队列）  
3. **消息队列**（如 RabbitMQ、Kafka）

### **栈的用途**
1. **函数调用栈**  
   ```python
   def func1():
       func2()  # 调用 func2 时，func1 的上下文入栈
   def func2():
       pass
   func1()
   ```
2. **括号匹配**  
   ```python
   def is_valid(s: str) -> bool:
       stack = []
       pairs = {")": "(", "]": "[", "}": "{"}
       for char in s:
           if char in pairs.values():
               stack.append(char)
           elif stack and stack[-1] == pairs[char]:
               stack.pop()
       return not stack
   ```
3. **浏览器前进/后退**  

---

## **3. 实现方式对比**
### **队列的实现**
- **Python推荐**：`collections.deque`（高效双端队列）  
  ```python
  from collections import deque
  q = deque()
  q.append(1)      # 入队
  q.popleft()      # 出队
  ```
- **不推荐**：用 `list.pop(0)`（时间复杂度 `O(n)`，性能差）

### **栈的实现**
- **Python推荐**：直接使用 `list`  
  ```python
  stack = []
  stack.append(1)  # 入栈
  stack.pop()      # 出栈
  ```
- 也可以用 `deque`，但无必要。

---

## **4. 常见面试题**
### **队列相关问题**
1. 用队列实现栈（LeetCode 225）
2. 用栈实现队列（LeetCode 232）
3. 滑动窗口最大值（LeetCode 239）

### **栈相关问题**
1. 有效的括号（LeetCode 20）
2. 最小栈（LeetCode 155）
3. 逆波兰表达式求值（LeetCode 150）

---

## **总结**
- **队列**：先入先出（FIFO），适用于顺序处理（如 BFS）。  
- **栈**：后入先出（LIFO），适用于回退操作（如递归、括号匹配）。  
- **Python 选择**：  
  - 队列 → `collections.deque`  
  - 栈 → `list`  

理解两者的区别能帮助你更高效地解决算法问题！ 🚀