from tree_utils import build_tree


# Обходить дерево пошуку в порядку зростання до k-го вузла.
def kthSmallest(root, k):
    stack = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right

    raise ValueError("k має бути від 1 до кількості вузлів")


if __name__ == "__main__":
    assert kthSmallest(build_tree([3, 1, 4, None, 2]), 1) == 1
    assert kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    print("OK")
