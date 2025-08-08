
class Trie:
    """
    11%&95%
    """
    def __init__(self):
        self.members_list = set()
        self.members_str = ''

    def insert(self, word: str) -> None:
        self.members_list.add(word)
        self.members_str += f",{word}"

    def search(self, word: str) -> bool:
        if word in self.members_list:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if f",{prefix}" in self.members_str:
            return True
        return False


class Trie_1:
    def __init__(self):
        self.children = [i for i in range(26)]
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


class Treenode:
    def __init__(self, val=None, children=dict()):
        self.val = val
        self.children = children
        self.is_end = False


class MyTrie:
    def __init__(self):
        self.root = Treenode(None, {})
        # 根结点没有任何的值 #根结点下面最多具有26个子结点
        # 根结点到子结点是以字符为key，node为value的dict

    def insert(self, word: str) -> None:
        node = self.root
        for x in word:
            if node.children.get(x, None):
                node = node.children[x]
            else:
                newnode = Treenode(x, {})
                node.children[x] = newnode
                node = newnode
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for x in word:
            if node.children.get(x, None):
                node = node.children[x]
            else:
                return False
        # 如果最后出来的时候node是叶子结点，则说明正确
        if node.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            if node.children.get(x, None):
                node = node.children[x]
            else:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.children = {}  # 存储子节点
        self.is_end = False  # 标记是否是单词的结尾


class TrieGPT:
    def __init__(self):
        self.root = TrieNode()  # 根节点

    def insert(self, word: str) -> None:
        """插入单词到前缀树"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """搜索单词是否在前缀树中"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """检查是否有单词以给定前缀开头"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    def tree_print(self):
        print()
        for i in self.root.children.items():
            print(i)

    def delete(self, word: str) -> None:
        """删除前缀树中的单词"""

        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                # 如果当前节点不是单词结尾，无需删除
                if not node.is_end:
                    return False
                node.is_end = False
                # 如果没有子节点，可以删除该节点
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_delete_child = _delete_helper(node.children[char], word, index + 1)

            if should_delete_child:
                del node.children[char]
                # 如果没有子节点且不是其他单词的结尾，可以删除该节点
                return len(node.children) == 0 and not node.is_end

            return False

        _delete_helper(self.root, word, 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def print_tree_horizontal(root, level=0):
    if root is not None:
        # print_tree_horizontal(root.children, level + 1)
        print(" " * 4 * level + "-> " + str(root.val))
        # print_tree_horizontal(root.left, level + 1)

if __name__ == "__main__":

    # a = Trie_1()
    # a = MyTrie()
    # a = TrieGPT()
    # res = a.insert('world')
    # print(res)
    # a.tree_print()
    trie = TrieGPT()
    trie.insert("apple")
    print(trie.search("apple"))    # 输出: True
    print(trie.search("app"))      # 输出: False
    print(trie.startsWith("app"))  # 输出: True
    trie.tree_print()
    trie.insert("app")
    print(trie.search("app"))      # 输出: True
    trie.delete("apple")
    print(trie.search("apple"))    # 输出: False

