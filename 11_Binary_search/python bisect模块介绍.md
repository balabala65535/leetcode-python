是的，Python 的 `bisect` 模块提供了多个用于**二分查找**和**插入**的函数，以下是完整的函数列表及其用途：

---

## 📚 `bisect` 模块函数一览

### 1. **查找类函数**
| 函数 | 别名 | 描述 | 特点 |
|------|------|------|------|
| `bisect_left(a, x)` | - | 返回 `x` 的**最左侧插入位置** | 如果 `x` 存在，返回第一个等于 `x` 的索引 |
| `bisect_right(a, x)` | `bisect` | 返回 `x` 的**最右侧插入位置** | 如果 `x` 存在，返回最后一个 `x` 的下一个位置 |

#### 示例：
```python
import bisect
arr = [1, 3, 3, 5, 7]

print(bisect.bisect_left(arr, 3))   # 输出 1（第一个3的位置）
print(bisect.bisect_right(arr, 3))  # 输出 3（最后一个3的下一个位置）
```

---

### 2. **插入类函数**
| 函数 | 描述 | 等价操作 |
|------|------|----------|
| `insort_left(a, x)` | 将 `x` 插入到 `a` 中**最左侧** | `a.insert(bisect_left(a, x), x)` |
| `insort_right(a, x)` | 将 `x` 插入到 `a` 中**最右侧** | `a.insert(bisect_right(a, x), x)` |
| `insort(a, x)` | `insort_right` 的别名 | - |

#### 示例：
```python
arr = [1, 3, 5]
bisect.insort_left(arr, 2)  # arr → [1, 2, 3, 5]
bisect.insort_right(arr, 3) # arr → [1, 2, 3, 3, 5]
```

---

## 🔍 关键区别：`left` vs `right`
| 场景 | `bisect_left`/`insort_left` | `bisect_right`/`insort_right` |
|------|----------------------------|-----------------------------|
| 当 `x` 存在于列表中时 | 返回/插入到**第一个 `x` 的位置** | 返回/插入到**最后一个 `x` 的下一个位置** |
| 当 `x` 不存在时 | 两者行为一致，返回/插入到合适位置 |

---

## 🛠️ 实际应用场景
### 1. **维护动态有序列表**
```python
sorted_list = []
for num in [3, 1, 4, 1, 5]:
    bisect.insort(sorted_list, num)  # 始终保持有序
# 结果: [1, 1, 3, 4, 5]
```

### 2. **范围统计**
```python
arr = [1, 2, 2, 3, 4]
# 统计 2 的个数
count = bisect.bisect_right(arr, 2) - bisect.bisect_left(arr, 2)  # 2
```

### 3. **离散化处理**（常用于算法竞赛）
```python
data = [100, 300, 200, 500]
sorted_data = sorted(data)
# 查询 200 的排名（从0开始）
rank = bisect.bisect_left(sorted_data, 200)  # 1
```

---

## ⚠️ 注意事项
1. **列表必须预先排序**，否则结果无意义
2. 所有函数的时间复杂度为 **O(log n)**
3. 插入操作 (`insort`) 的**实际复杂度是 O(n)**，因为列表插入需要移动元素

---

## 🌟 为什么选择 `bisect`？
- 比手动实现二分更**安全**（避免边界错误）
- 比线性查找更**高效**（O(log n) vs O(n)）
- 接口简洁，适合**快速原型开发**

如果需要更复杂的二分逻辑（如自定义比较函数），可以考虑 `functools.cmp_to_key` 或实现自己的二分函数。
