from typing import *
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            my_dict.setdefault(i, 0)
            my_dict[i] += 1
        myheap = []
        for i in my_dict:
            heapq.heappush(myheap, (my_dict[i], i))
            if len(myheap) > k:
                heapq.heappop(myheap)
        return [i[-1] for i in myheap]


import heapq
from collections import Counter


def topKFrequent(nums, k):
    # 统计元素频率
    count = Counter(nums)

    # 使用最小堆维护前k高频元素
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # 提取结果
    return [num for freq, num in heap]


# 示例
nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2
print(topKFrequent(nums, k))  # 输出: [3, 1]

from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# 示例
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))  # 输出: [1, 2]