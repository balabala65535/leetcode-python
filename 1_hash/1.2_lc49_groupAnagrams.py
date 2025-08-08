class Solution(object):
    def groupAnagrams(self, strs):
        """
        含相同字母
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        all_list = {}
        for my_index, i in enumerate(strs):
            word_list = list(set(list(i)))
            word_list.sort()
            word_list_key = ''.join(word_list)
            all_list.setdefault(word_list_key, [])
            all_list[word_list_key].append(i)
        arrange_result = [all_list[i] for i in all_list]
        return arrange_result

    def groupAnagrams_2(self, strs):
        """
        字母异位词：长度相同，并且各种字母个数也想同
        :type strs: List[str]
        :rtype: List[List[str]]
        时间：19ms，击败84.83%
        空间：15.66MB, 93.66%
        去掉arrange_result = [all_list[i] for i in all_list]
        时间：16ms，击败 89.20%
        空间：15.95MB, 37.60%
        #去掉list(i)
        """
        all_list = {}
        for my_index, i in enumerate(strs):
            word_list = list(i)
            word_list.sort()
            word_list_key = ''.join(word_list)
            all_list.setdefault(word_list_key, [])
            all_list[word_list_key].append(i)
        return list(all_list.values())

    def groupAnagrams_3(self, strs):
        dic = {}
        for element in strs:
            t = ''.join(sorted(element))
            if t in dic:
                dic[t].append(element)
            else:
                dic[t] = [element]
        return list(dic.values())

    def groupAnagrams_4(self, strs):
        """
        方法 1：使用 collections.defaultdict + 字符计数（推荐）
        :return:
        """
        from collections import defaultdict
        anagrams = defaultdict(list)
        for word in strs:
            # 使用字符计数作为键（避免排序）
            count = [0] * 26  # 假设只有小写字母
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)  # 列表不可哈希，转为元组
            print(key)
            anagrams[key].append(word)
        return list(anagrams.values())

    def groupAnagrams_5(self, strs):
        """
        set/frozenset 的相等性只取决于元素内容，与顺序无关。

        tuple 作为 frozenset 的元素是允许的，因为 tuple 是不可变的（可哈希）。
        如果换成 list（可变，不可哈希），则无法放入 frozenset 中，会报错。

        tuple和frozenset的区别：
        1.tuple是有序的，而frozenset是无序的；
        2.tuple有操作元素的方法，而frozenset没有；
        3.查询的速度o(n), O(1)

        set和frozenset的区别：
        1.set是可变的，而frozenset是不可变；
        2.set不可hash,而frozenset可hash;
        3.内存占用set稍大，frozenset稍小；
        4.set的元素操作方法，frozenset没有；
        :param strs:
        :return:
        """
        from collections import defaultdict, Counter
        anagrams = defaultdict(list)
        for word in strs:
            key = frozenset(Counter(word).items())  # Counter 统计字符频率
            # key = tuple(Counter(word).items())  # Counter 统计字符频率
            # key = frozenset(Counter(word))  # Counter 统计字符频率
            print(key)
            anagrams[key].append(word)
        return list(anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["ddddddddddg","dgggggggggg"]
    a = Solution()
    # resp = a.groupAnagrams(strs)
    # resp = a.groupAnagrams_2(strs)
    # resp = a.groupAnagrams_4(strs)
    resp = a.groupAnagrams_5(strs)
    print(resp)