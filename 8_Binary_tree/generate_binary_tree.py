from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(data):
    if not data:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        current = queue.popleft()
        if data[i] is not None:
            current.left = TreeNode(data[i])
            queue.append(current.left)
        i += 1
        if i < len(data) and data[i] is not None:
            current.right = TreeNode(data[i])
            queue.append(current.right)
        i += 1

    return root


def print_tree(root, level=0, label="."):
    if root is not None:
        print_tree(root.right, level + 1, "R")
        print("   " * level + f"{label}: {root.val}")
        print_tree(root.left, level + 1, "L")


def print_tree_horizontal(root, level=0):
    if root is not None:
        print_tree_horizontal(root.right, level + 1)
        print(" " * 4 * level + "-> " + str(root.val))
        print_tree_horizontal(root.left, level + 1)


def print_tree_1(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        print_tree(root.left, level + 1, "├── ")
        print_tree(root.right, level + 1, "└── ")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    tree = build_tree_from_list(arr)

