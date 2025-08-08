
# Python `heapq` 模块详解

`heapq` 是 Python 的一个内置模块，提供了堆队列算法的实现（也称为优先队列算法）。它使用小顶堆（min-heap）数据结构，可以高效地进行元素的插入和提取最小值的操作。

## 基本特性

1. **小顶堆**：父节点的值总是小于或等于其子节点的值
2. **就地操作**：所有函数都是在原列表上操作，不返回新列表
3. **时间复杂度**：
   - 插入元素：O(log n)
   - 弹出最小元素：O(log n)
   - 获取最小元素：O(1)

## 主要函数

### 1. `heapq.heappush(heap, item)`
将元素 `item` 压入堆 `heap` 中，保持堆结构不变。

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
print(heap)  # 输出: [1, 5, 2]
```

### 2. `heapq.heappop(heap)`
弹出并返回堆 `heap` 中的最小元素，保持堆结构不变。

```python
min_val = heapq.heappop(heap)
print(min_val)  # 输出: 1
print(heap)     # 输出: [2, 5]
```

### 3. `heapq.heapify(x)`
将列表 `x` 原地转换为堆结构，时间复杂度为 O(n)。

```python
nums = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(nums)
print(nums)  # 输出: [1, 1, 2, 3, 5, 9, 4]
```

### 4. `heapq.heappushpop(heap, item)`
先将 `item` 压入堆，然后弹出并返回最小元素，比先 `heappush()` 再 `heappop()` 更高效。

```python
min_val = heapq.heappushpop(heap, 3)
print(min_val)  # 输出: 2
print(heap)     # 输出: [3, 5]
```

### 5. `heapq.heapreplace(heap, item)`
先弹出最小元素，然后压入新元素 `item`。

```python
min_val = heapq.heapreplace(heap, 4)
print(min_val)  # 输出: 3
print(heap)     # 输出: [4, 5]
```

### 6. `heapq.nlargest(n, iterable[, key])`
返回可迭代对象中前 n 个最大的元素。

```python
print(heapq.nlargest(2, [1, 2, 3, 4, 5]))  # 输出: [5, 4]
```

### 7. `heapq.nsmallest(n, iterable[, key])`
返回可迭代对象中前 n 个最小的元素。

```python
print(heapq.nsmallest(2, [1, 2, 3, 4, 5]))  # 输出: [1, 2]
```

## 自定义对象排序

可以通过元组或实现 `__lt__` 方法来处理自定义对象：

```python
# 方法1：使用元组 (priority, item)
heap = []
heapq.heappush(heap, (2, 'code'))
heapq.heappush(heap, (1, 'eat'))
heapq.heappush(heap, (3, 'sleep'))

print(heapq.heappop(heap)[1])  # 输出: 'eat'

# 方法2：实现 __lt__ 方法
class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
    
    def __lt__(self, other):
        return self.priority < other.priority

heap = []
heapq.heappush(heap, Task(2, 'code'))
heapq.heappush(heap, Task(1, 'eat'))
heapq.heappush(heap, Task(3, 'sleep'))

print(heapq.heappop(heap).description)  # 输出: 'eat'
```

## 实际应用示例

### 1. 合并多个有序列表

```python
def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    for i, array in enumerate(sorted_arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))
    
    result = []
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        if elem_idx + 1 < len(sorted_arrays[arr_idx]):
            next_elem = sorted_arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, arr_idx, elem_idx + 1))
    return result

arrays = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]
print(merge_sorted_arrays(arrays))  # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

### 2. 实现优先队列

```python
class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0  # 用于处理优先级相同的元素
    
    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._heap)[-1]

pq = PriorityQueue()
pq.push('task1', 2)
pq.push('task2', 1)
pq.push('task3', 2)

print(pq.pop())  # 输出: 'task2' (优先级最高)
print(pq.pop())  # 输出: 'task1' (与task3同优先级，但先加入)
```

## 注意事项

1. `heapq` 模块只实现了小顶堆，如果需要大顶堆，可以将数值取反后存储
2. 堆操作会直接修改原列表，而不是返回新列表
3. 堆结构不保证完全有序，只保证堆顶是最小元素
4. 对于大型数据集，`nlargest()` 和 `nsmallest()` 比排序后再切片更高效


# `heapq` 在算法中的应用详解

`heapq` 模块因其高效的优先级队列操作特性，在算法设计中有着广泛的应用。以下是它在各类算法问题中的典型应用场景和实现方式：

## 一、基础应用场景

### 1. Top K 问题
**问题类型**：从海量数据中找出最大/最小的K个元素

```python
def top_k_smallest(nums, k):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(k)]

def top_k_largest(nums, k):
    # 使用负号模拟大顶堆
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)
    return [-heapq.heappop(max_heap) for _ in range(k)]
```

**时间复杂度**：O(n + k log n)  
比完全排序O(n log n)更高效，特别当k≪n时

### 2. 流数据的中位数
**问题类型**：动态维护数据流的中位数

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # 大顶堆（存较小一半）
        self.large = []  # 小顶堆（存较大一半）

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        return self.large[0]
```

## 二、图算法应用

### 3. Dijkstra最短路径算法
**核心作用**：高效获取当前距离起点最近的节点

```python
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > distances[u]:
            continue
        for v, weight in graph[u].items():
            distance = current_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(heap, (distance, v))
    return distances
```

**优势**：将时间复杂度从O(V²)优化到O(E + V log V)

### 4. Prim最小生成树算法
**核心作用**：动态选择权重最小的边

```python
def prim(graph):
    mst = []
    visited = set()
    start_node = next(iter(graph))
    heap = [(weight, start_node, neighbor) 
            for neighbor, weight in graph[start_node].items()]
    heapq.heapify(heap)
    visited.add(start_node)
    
    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (w, v, neighbor))
    return mst
```

## 三、高级应用场景

### 5. 合并K个有序链表
**LeetCode 23**：高效合并多个已排序序列

```python
def mergeKLists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i))
    
    dummy = ListNode()
    curr = dummy
    while heap:
        val, i = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[i].next:
            lists[i] = lists[i].next
            heapq.heappush(heap, (lists[i].val, i))
    return dummy.next
```

**时间复杂度**：O(N log k)，其中N是总节点数，k是链表数量

### 6. 任务调度问题
**贪心算法**：合理安排任务执行顺序

```python
def leastInterval(tasks, n):
    freq = collections.Counter(tasks)
    max_heap = [-cnt for cnt in freq.values()]
    heapq.heapify(max_heap)
    
    time = 0
    while max_heap:
        cycle = []
        for _ in range(n + 1):
            if max_heap:
                cycle.append(heapq.heappop(max_heap))
        
        for cnt in cycle:
            if cnt + 1 < 0:
                heapq.heappush(max_heap, cnt + 1)
        
        time += len(cycle) if not max_heap else n + 1
    return time
```

## 四、特殊问题优化

### 7. 滑动窗口最大值
**单调堆优化**（虽然双端队列更优，但堆也可实现）：

```python
def maxSlidingWindow(nums, k):
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-nums[i], i))
    
    result = [-heap[0][0]]
    for i in range(k, len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        result.append(-heap[0][0])
    return result
```

### 8. 数据流中的第K大元素
**LeetCode 703**：动态维护K大小的堆

```python
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

## 五、性能优化技巧

1. **元组比较优化**：当优先级相同时，添加辅助比较字段
   ```python
   heapq.heappush(heap, (priority, index, item))
   ```

2. **批量建堆**：使用`heapify`(O(n))比逐个`heappush`(O(n log n))更高效

3. **惰性删除**：对于需要删除非堆顶元素的场景
   ```python
   while heap and heap[0] in deleted:
       heapq.heappop(heap)
   ```

4. **内存优化**：对于超大数据集，考虑使用`nsmallest`/`nlargest`的迭代器版本

## 六、与其他数据结构的对比

| 场景                | 适用数据结构 | 时间复杂度       | 优势                          |
|---------------------|--------------|------------------|-------------------------------|
| 频繁获取极值        | 堆           | O(1)获取         | 动态维护                      |
| 需要完全排序        | 有序数组     | O(n log n)构建   | 支持二分查找                  |
| 频繁随机访问        | 普通数组     | O(1)访问         | 内存连续                      |
| 需要范围查询        | 平衡二叉搜索树| O(log n)操作     | 支持复杂查询                  |

`heapq`最适合需要频繁插入和提取最小值/最大值的场景，特别是当数据动态变化时。