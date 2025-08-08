
from typing import *


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord("a")])
            print(ch, i, end)
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
            print(partition)

        return partition


if __name__ == "__main__":
    s = "aabbcc"
    a = Solution()
    resp = a.partitionLabels(s)
    print(resp)

