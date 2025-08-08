from typing import *
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        方法二：单调队列
        为了可以同时弹出队首和队尾的元素，我们需要使用双端队列。满足这种单调性的双端队列一般称作「单调队列」。
        """
        from collections import deque
        length = len(nums)
        max_num = []
        # 形成窗口
        res_que = deque()
        for i in range(k):
            while res_que and res_que[-1] < nums[i]:
                res_que.pop()
            res_que.append(nums[i])
        max_num.append(res_que[0])
        # 窗口
        for i in range(k, length):
            if res_que[0] == nums[i - k]:
                res_que.popleft()
            while res_que and res_que[-1] < nums[i]:
                res_que.pop()
            res_que.append(nums[i])
            max_num.append(res_que[0])
        return max_num


def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    length = len(nums)
    if k > length:
        k = length
    max_list = []
    for my_index, i in enumerate(nums):
        if my_index > length - k:
            continue
        my_max = max(nums[my_index: my_index + k])
        max_list.append(my_max)
    return max_list


def maxSlidingWindow_1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    max_list = []
    length = len(nums)

    max_list = [max(nums[:k])]
    for i in range(1, length - k + 1):
        max_num = max(nums[i: i + k])
        max_list.append(max_num)
    return max_list


def maxSlidingWindow_2(nums, k):
    """
    优先队列(对)
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    # 注意 Python 默认的优先队列是小根堆, -value 最小值为权重
    q = [(-nums[i], i) for i in range(k)]
    heapq.heapify(q)

    ans = [-q[0][0]]
    for i in range(k, n):
        print(f"index:「{i}")
        heapq.heappush(q, (-nums[i], i))  # 添加元素
        print(q, i - k, '>=', q[0][1])
        while q[0][1] <= i - k:  # q[0][1]
            print(q, i - k, "^^")
            heapq.heappop(q)  #  弹出最大值,实际为最小值，需要保障list里的元素个数为i-k个，
            # 为什么要popout是为了保障队列里 最好只有3个值，大于3个说明最大值在第一个；
            # 否则最大值就会多余3个，且前面队列的最大值也包含在本次滑动窗口范围内
            print("now:",q)
        ans.append(-q[0][0])
        print(ans)
        print("==="*5)

    return ans


def maxSlidingWindow_3(nums, k):
    """
    单调队列
    collections.deque（双端队列）是 Python 标准库中一个高性能的容器数据类型，它支持从两端快速添加和删除元素。与普通列表(list)相比，deque 在某些操作上具有显著优势。
    我悟了， 队尾比不过同龄人的删掉，队头超出时代区间的删掉，历史就是这么不断更迭的。
    思路：1.因此我们可以使用一个队列存储所有还没有被移除的下标。在队列中，这些下标按照从小到大的顺序被存储，并且它们在数组 nums 中对应的值是严格单调递减的。
    2.nums[i] > nums[j],相邻且单增不能被移除；
    3.当滑动窗口向右移动时，我们需要把一个新的元素放入队列中。为了保持队列的性质，我们会不断地将新的元素与队尾的元素相比较，如果前者大于等于
    后者，那么队尾的元素就可以被永久地移除，我们将其弹出队列。我们需要不断地进行此项操作，直到队列为空或者新的元素小于队尾的元素。
    4.严格单调递减的，因此此时队首下标对应的元素就是滑动窗口中的最大值。但与方法一中相同的是，此时的最大值可能在滑动窗口左边界的左侧，并且随着窗口向右移动，它永远不可能出现在滑动窗口中了
    :param nums:
    :param k:
    :return:
    """
    import collections
    n = len(nums)
    q = collections.deque()  # 保存数的index

    # 先排前面K个数，以获得它最大值
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:  # 当前的值，大于了之前队列里的最小索引值(即：前一个值)，前一个值就会被删除
            q.pop()  # 弹出最后一个，即最小值
        q.append(i)
    print([i for i in q])

    # 再排K及k后面的数
    ans = [nums[q[0]]]
    for i in range(k, n):
        while q and nums[i] >= nums[q[-1]]:  # 当前的值，大于了之前队列里的最小索引值(即：前一个值)，前一个值就会被删除
            q.pop()
        q.append(i)
        print(q)
        while q[0] <= i - k:  # 超出了序列范围，则移调
            q.popleft()
        ans.append(nums[q[0]])

    return ans



def maxSlidingWindow_4(nums, k):
    """
    分块 + 预处理
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    prefixMax, suffixMax = [0] * n, [0] * n
    for i in range(n):
        if i % k == 0:
            prefixMax[i] = nums[i]
        else:
            prefixMax[i] = max(prefixMax[i - 1], nums[i])
    for i in range(n - 1, -1, -1):
        if i == n - 1 or (i + 1) % k == 0:
            suffixMax[i] = nums[i]
        else:
            suffixMax[i] = max(suffixMax[i + 1], nums[i])

    print('prefixMax', prefixMax)
    print('suffixMax', suffixMax)
    ans = [max(suffixMax[i], prefixMax[i + k - 1]) for i in range(n - k + 1)]
    return ans


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    # nums = [9,8,7,6,5,4,3,2,1,0]
    nums = [-124, 14, -6,1, 0, 0, 0,  7, 8, 9, 10]
    # nums = [0, 1, 2, 3, 4, 5]
    k = 20

    # nums = [1]
    # k = 4

    # resp = maxSlidingWindow(nums, k)
    resp = maxSlidingWindow_1(nums, k)
    print(resp)
    # resp = maxSlidingWindow_3(nums, k)
    resp = maxSlidingWindow_4(nums, k)
    print(resp)