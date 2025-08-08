
### 链表解题经典三板斧，哑巴节点，栈，快慢指针

----
### Python 中链表的创建与操作方法

#### 1. 链表节点的定义
在 Python 中，链表节点通常用类来表示：
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val    # 节点值
        self.next = next  # 指向下一个节点的指针
```

#### 2. 创建链表
**方法一：手动连接节点**
```python
# 创建节点
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# 连接节点
node1.next = node2
node2.next = node3
head = node1  # 头节点
```

**方法二：从列表创建链表**
```python
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

head = create_linked_list([1, 2, 3])  # 1->2->3
```

#### 3. 链表基本操作

**（1）遍历链表**
```python
def traverse(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

traverse(head)  # 输出：1 -> 2 -> 3 -> None
```

**（2）获取链表长度**
```python
def get_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
```

**（3）插入节点**
```python
# 在指定位置插入
def insert_node(head, index, val):
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(index):
        if not prev.next:
            break
        prev = prev.next
    new_node = ListNode(val, prev.next)
    prev.next = new_node
    return dummy.next
```

**（4）删除节点**
```python
# 删除指定值的节点
def delete_node(head, val):
    dummy = ListNode(0, head)
    prev, current = dummy, head
    while current:
        if current.val == val:
            prev.next = current.next
            break
        prev, current = current, current.next
    return dummy.next
```

#### 4. 常见算法操作

**（1）反转链表**
```python
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

**（2）检测环**
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**（3）合并两个有序链表**
```python
def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next
```

#### 5. 实用工具函数

**（1）链表转列表**
```python
def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
```

**（2）可视化链表**
```python
def visualize(head):
    arrows = []
    while head:
        arrows.append(str(head.val))
        if head.next:
            arrows.append("→")
        head = head.next
    print(" ".join(arrows) if arrows else "Empty List")
```

#### 6. 注意事项
1. **边界条件**：总是考虑空链表（`head is None`）的情况
2. **指针操作**：修改链表时注意不要丢失节点引用
3. **虚拟头节点**：使用 `dummy` 节点可以简化头节点的特殊处理
4. **递归方法**：许多链表问题也可以用递归解决，但需要注意栈溢出风险

#### 7. 复杂度分析
| 操作         | 时间复杂度 | 空间复杂度 |
|--------------|------------|------------|
| 访问第k个节点 | O(n)       | O(1)       |
| 插入/删除节点 | O(n)       | O(1)       |
| 反转链表      | O(n)       | O(1)       |
| 检测环        | O(n)       | O(1)       |

#### 示例使用
```python
# 创建链表 1->2->3
head = create_linked_list([1, 2, 3])

# 在位置1插入4（变为1->4->2->3）
head = insert_node(head, 1, 4)

# 删除值为2的节点（变为1->4->3）
head = delete_node(head, 2)

# 反转链表（变为3->4->1）
head = reverse_list(head)

visualize(head)  # 输出：3 → 4 → 1
```

---
### 链表中的值是否可以重复？

**答案：是的，链表中的值可以重复**。链表节点的值（`val`）和节点本身是两个不同的概念：

#### 1. **值的重复性**
- 多个不同节点可以存储相同的值
- 例如：`1 → 2 → 2 → 3` 是完全合法的链表
- 这与列表（list）的特性一致，允许重复元素

#### 2. **节点的唯一性**
- 每个链表节点是独立的内存对象
- 即使值相同，不同节点的内存地址也不同
- 示例：
  ```python
  node1 = ListNode(2)
  node2 = ListNode(2)
  print(node1 == node2)  # 输出 False（不同对象）
  print(node1.val == node2.val)  # 输出 True（值相同）
  ```

#### 3. 实际应用中的影响
| 场景                 | 值重复的影响                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **按值搜索**         | 需要遍历所有节点（可能找到多个匹配节点）                                      |
| **删除操作**         | 需明确是删除第一个匹配值/全部匹配值/特定位置的节点                            |
| **哈希表存储节点**   | 需注意存储的是节点对象（内存地址唯一），而不是值                              |

#### 4. 示例代码演示
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建含重复值的链表：1 → 2 → 2 → 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

# 查找所有值为2的节点
def find_all(head, target):
    results = []
    current = head
    while current:
        if current.val == target:
            results.append(current)
        current = current.next
    return results

matches = find_all(head, 2)
print(f"找到 {len(matches)} 个值为2的节点")  # 输出：找到 2 个值为2的节点
```

#### 5. 何时需要值唯一？
如果需要强制值唯一性，可以：
1. 在插入时检查是否已存在相同值
   ```python
   def insert_unique(head, val):
       current = head
       while current:
           if current.val == val:
               return False  # 值已存在
           current = current.next
       new_node = ListNode(val, head)
       return new_node  # 返回新头节点
   ```
2. 使用辅助集合记录已存在的值

#### 6. 总结
- **可以重复**：链表设计本身不限制节点值的重复性
- **操作注意**：处理重复值时要明确需求（如删除第一个还是全部）
- **节点唯一**：即使值相同，不同节点仍是独立对象

这种灵活性使链表能适用于更多场景，但也要求开发者更谨慎地处理重复值情况。