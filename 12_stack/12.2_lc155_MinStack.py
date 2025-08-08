

"""
栈结构先进后出的性质。
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')  # 当前最小值

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append(0)  # 第一个元素的差值为0
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if diff < 0:  # 说明val比当前min_val小
                self.min_val = val

    def pop(self) -> None:
        if not self.stack:
            return None

        diff = self.stack.pop()
        if diff < 0:
            # 需要恢复前一个min_val
            popped_val = self.min_val
            self.min_val = popped_val - diff
            return popped_val
        else:
            return self.min_val + diff

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.min_val  # 当前元素就是最小值
        else:
            return self.min_val + diff

    def getMin(self) -> int:
        return self.min_val


# 测试示例
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # 输出 -3
min_stack.pop()
print(min_stack.top())  # 输出 0
print(min_stack.getMin())  # 输出 -2
