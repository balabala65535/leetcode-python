### **Python 中的堆（Heap）**
堆（Heap）是一种特殊的**完全二叉树**数据结构，满足以下性质：
- **最小堆（Min-Heap）**：每个节点的值 ≤ 其子节点的值（堆顶是最小值）。  
- **最大堆（Max-Heap）**：每个节点的值 ≥ 其子节点的值（堆顶是最大值）。  

Python 的 `heapq` 模块提供了堆的实现，但默认仅支持**最小堆**。若需要最大堆，需通过存储相反数间接实现。

---

## **1. 堆的基本操作**
`heapq` 模块提供以下核心函数（均操作于列表）：
| 函数                     | 说明                                                                 |
|--------------------------|----------------------------------------------------------------------|
| `heapq.heappush(heap, x)` | 将元素 `x` 加入堆，保持堆属性。                                      |
| `heapq.heappop(heap)`     | 弹出堆顶元素（最小值），并重新调整堆。                               |
| `heapq.heapify(heap)`     | 将普通列表转换为堆（原地修改，时间复杂度 O(n)）。                    |
| `heapq.heappushpop(heap, x)` | 先 `heappush` 再 `heappop`，比分开调用高效。                        |
| `heapq.heapreplace(heap, x)` | 先 `heappop` 再 `heappush`，需保证堆非空。                          |
| `heapq.nlargest(k, iterable)` | 返回可迭代对象中前 `k` 个最大元素（无需构建完整堆）。               |
| `heapq.nsmallest(k, iterable)` | 返回可迭代对象中前 `k` 个最小元素（无需构建完整堆）。               |

---

## **2. 代码示例**
### **(1) 最小堆（默认）**
```python
import heapq

# 创建一个堆（通常用列表表示）
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)

print(heap)          # 输出 [1, 2, 4, 3]（堆结构，不必有序）
print(heapq.heappop(heap))  # 输出 1（弹出最小值）
print(heap)          # 输出 [2, 3, 4]（自动调整）
```

### **(2) 最大堆（通过存储相反数实现）**
```python
import heapq

heap = []
nums = [3, 1, 4, 2]
# 存储相反数模拟最大堆
for num in nums:
    heapq.heappush(heap, -num)

print([-x for x in heap])  # 输出 [4, 2, 3, 1]（堆结构）
print(-heapq.heappop(heap))  # 输出 4（弹出最大值）
```

### **(3) 堆化现有列表**
```python
import heapq

nums = [3, 1, 4, 2]
heapq.heapify(nums)  # 原地转换为堆
print(nums)         # 输出 [1, 2, 4, 3]（堆结构）
```

### **(4) 高效合并堆操作**
```python
import heapq

heap = [1, 3, 5]
heapq.heappushpop(heap, 2)  # 先 push 2，再 pop 最小值（1）
print(heap)                 # 输出 [2, 3, 5]

heapq.heapreplace(heap, 0)  # 先 pop 最小值（2），再 push 0
print(heap)                 # 输出 [0, 3, 5]
```

### **(5) 获取前 K 大/小元素（无需构建堆）**
```python
import heapq

nums = [3, 1, 4, 2, 5]
print(heapq.nlargest(3, nums))  # 输出 [5, 4, 3]（前3大）
print(heapq.nsmallest(2, nums)) # 输出 [1, 2]（前2小）
```

---

## **3. 堆的应用场景**
1. **优先级队列**：任务调度（总优先处理最小/最大任务）。  
2. **Top K 问题**：如“前 K 个高频元素”（结合哈希表统计频率）。  
3. **合并有序序列**：多路归并（如合并 K 个有序链表）。  
4. **Dijkstra 算法**：图的最短路径优化（优先扩展最小权值节点）。  

---

## **4. 注意事项**
1. **直接操作列表无效**：必须通过 `heapq` 函数维护堆属性。  
2. **最大堆需取反**：Python 无内置最大堆，需手动存储 `-x`。  
3. **元素需可比较**：若堆存储元组，默认按第一个元素比较。  
   ```python
   heapq.heappush(heap, (priority, value))  # 按 priority 排序
   ```

---

## **5. 时间复杂度**
| 操作            | 时间复杂度  |
|-----------------|------------|
| 建堆 (`heapify`) | O(n)       |
| 插入 (`heappush`) | O(log n)   |
| 弹出 (`heappop`) | O(log n)   |
| 获取堆顶        | O(1)       |

---

### **总结**
- Python 的 `heapq` 模块简单易用，但仅支持最小堆。  
- 最大堆需通过存储相反数间接实现。  
- 适合解决**动态数据流中的 Top K 问题**或**优先级调度**场景。  

如果需要更复杂的堆（如自定义比较函数），可手动实现或使用 `PriorityQueue`（线程安全版本）。

---

### **Python `heapq` 模块的时间复杂度分析**

`heapq` 是 Python 提供的**最小堆（Min-Heap）**实现，基于**完全二叉树**结构，核心操作的时间复杂度如下：

| **操作**               | **时间复杂度** | **说明**                                                                 |
|------------------------|---------------|--------------------------------------------------------------------------|
| **`heapify(heap)`**     | **O(n)**       | 将普通列表原地转换为堆（自底向上调整）。                                 |
| **`heappush(heap, x)`** | **O(log n)**   | 向堆中插入一个元素，并保持堆属性。                                       |
| **`heappop(heap)`**     | **O(log n)**   | 弹出堆顶元素（最小值），并重新调整堆。                                   |
| **`heappushpop(heap, x)`** | **O(log n)** | 先 `heappush` 再 `heappop`（比分开调用高效）。                           |
| **`heapreplace(heap, x)`** | **O(log n)** | 先 `heappop` 再 `heappush`（需保证堆非空）。                             |
| **`nsmallest(k, iterable)`** | **O(n log k)** | 返回可迭代对象中前 `k` 个最小元素（无需构建完整堆）。                   |
| **`nlargest(k, iterable)`**  | **O(n log k)** | 返回可迭代对象中前 `k` 个最大元素（无需构建完整堆）。                   |

---

### **关键点解析**
1. **`heapify` 的 O(n) 时间复杂度**  
   - 表面上看，堆的构建似乎需要 O(n log n)（因为每个元素的插入是 O(log n)），但实际通过**自底向上调整**（从最后一个非叶子节点开始），可以将时间复杂度优化到 **O(n)**。  
   - 数学证明：  
     - 最坏情况下，所有叶子节点（占约 n/2）无需调整，其他节点的调整次数与其高度相关，总操作次数为：  
       \[
       \sum_{h=0}^{\log n} \frac{n}{2^{h+1}} \cdot h \leq n \sum_{h=0}^{\log n} \frac{h}{2^h} = O(n)
       \]

2. **`heappush` 和 `heappop` 的 O(log n)**  
   - 插入或删除元素后，需要从当前节点向上或向下调整堆，最多操作树的高度（即 **log n** 次）。

3. **`nsmallest/nlargest` 的 O(n log k)**  
   - 使用大小为 `k` 的堆维护结果：  
     - 遍历所有 `n` 个元素，每次插入/弹出的时间复杂度为 O(log k)。  
   - 若 `k` 接近 `n`，退化为 O(n log n)。  

4. **堆顶访问是 O(1)**  
   - 直接访问 `heap[0]` 即可（无需调整堆）。

---

### **与其他数据结构的对比**
| **操作**       | **堆 (`heapq`)** | **有序列表 (`list.sort`)** | **平衡二叉搜索树** |
|----------------|------------------|---------------------------|--------------------|
| **插入**       | O(log n)         | O(n)                      | O(log n)           |
| **删除最小值** | O(log n)         | O(1)（但插入代价高）       | O(log n)           |
| **构建**       | O(n)             | O(n log n)                | O(n log n)         |
| **Top K 查询** | O(n log k)       | O(1)（但需预排序）         | O(k log n)         |

---

### **实际应用建议**
1. **动态数据流中的 Top K 问题**  
   - 使用堆（如 `nsmallest/nlargest`）避免全量排序。  
   - 示例：实时统计高频词。  
   ```python
   import heapq
   data_stream = [5, 2, 9, 1, 7, 3]
   top_3 = heapq.nlargest(3, data_stream)  # O(n log 3)
   ```

2. **优先级队列**  
   - 结合 `heappush` 和 `heappop` 实现任务调度。  
   ```python
   tasks = []
   heapq.heappush(tasks, (2, "Task A"))  # (priority, task)
   heapq.heappush(tasks, (1, "Task B"))
   print(heapq.heappop(tasks)[1])        # 输出 "Task B"（优先级更高）
   ```

3. **最大堆的实现**  
   - 通过存储相反数模拟最大堆：  
   ```python
   max_heap = []
   heapq.heappush(max_heap, -x)  # 插入时取负
   max_value = -heapq.heappop(max_heap)  # 弹出时再取反
   ```

---

### **总结**
- **`heapq` 适合动态维护极值**，尤其在数据量较大或需要实时更新时。  
- **时间复杂度优势**：  
  - 插入/删除：O(log n) vs 列表的 O(n)。  
  - 构建堆：O(n) vs 排序的 O(n log n)。  
- **局限性**：  
  - 不支持直接访问中间元素（堆仅保证堆顶是最小值）。  
  - 原生不支持最大堆（需取反实现）。