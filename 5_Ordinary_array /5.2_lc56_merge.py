
def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    result = [intervals[0]]
    for i in intervals[1:]:
        if result[-1][0] <= i[0] <= result[-1][1]:
            if i[1] > result[-1][1]:
                result[-1][1] = i[1]
        if result[-1][0] <= i[1] <= result[-1][1]:
            if i[0] < result[-1][0]:
                result[-1][0] = i[0]
        elif i[1] > result[-1][1]:
            result[-1][1] = i[1]
        else:
            result.append(i)

    return result


def merge_1(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in intervals[1:]:
        # 判断2个区间是否有交集
        if max(result[-1][0], i[0]) <= min(result[-1][1], i[1]):
            result[-1][0] = min(result[-1][0], i[0])
            result[-1][1] = max(result[-1][1], i[1])
        else:
            result.append(i)
    return result


def merge_2(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # intervals = [[1, 4], [0, 4]]
    intervals = [[1, 4], [0, 45]]
    intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    # resp = merge(intervals)
    resp = merge_1(intervals)
    print(resp)