"""
堆是一种非常实用的数据结构，特别适合需要频繁访问最大或最小元素的场景。
堆不会自动维护完全有序的数组，它只保证堆顶元素是最大/最小值，以及父子节点之间的特定顺序关系。
这种"部分有序"的特性使得堆在实现优先队列和解决Top K问题等方面非常高效，因为不需要维护完全排序的开销。
"""
import heapq


def find_kth_largest(nums, k):
    # 构建最小堆，堆的大小保持为k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # 弹出最小的元素
    return heap[0]  # 堆顶就是第k大的元素


# 示例
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_largest(nums, k))  # 输出: 4

import random


def find_kth_largest(nums, k):
    """
    快速选择算法（平均O(n)时间复杂度）
    :param nums:
    :param k:
    :return:
    """

    def quickselect(left, right, k_smallest):
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    return quickselect(0, len(nums) - 1, len(nums) - k)


# 示例
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))  # 输出: 5


class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot

        return quick_select(nums, k)

    def findKthLargest(self, nums, k):
        """
        方法 1：快速选择（Quickselect）
        思路：
        类似快排的分区过程，但每次只递归处理包含第 K 大元素的那一部分。
        分区后，根据基准的位置与 K 的关系决定继续处理左半部分还是右半部分。
        """
        import random

        def quickselect(left, right, k_smallest):
            # 随机选择基准（避免最坏情况）
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            # 将基准交换到最右端
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 分区：将大于基准的元素移到左侧
            store_index = left
            for i in range(left, right):
                if nums[i] > pivot:  # 注意：这里是找第 K 大，所以用 >
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 将基准交换到正确位置
            nums[right], nums[store_index] = nums[store_index], nums[right]

            # 判断基准的位置是否为第 k-1 个（0-based）
            if store_index == k_smallest:
                return nums[store_index]
            elif store_index < k_smallest:
                return quickselect(store_index + 1, right, k_smallest)
            else:
                return quickselect(left, store_index - 1, k_smallest)

        # 第 K 大元素在排序后的数组中的索引是 len(nums) - k（0-based）
        return quickselect(0, len(nums) - 1, k - 1)

    # 示例
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))  # 输出 5
