# 回溯法
## 是一种暴力搜索，及递归函数
1,抽象为对应的树形结构
2.回溯法模版

```python
def backtrack(path, choices):
    if 满足条件:
        记录结果
        return
    for 选择 in choices:
        做选择  # 处理节点
        backtrack(path, new_choices)  # 递归
        撤销选择  # 取消处理
```

