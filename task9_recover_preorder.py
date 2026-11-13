import re

from tree_utils import TreeNode, tree_to_list


# Визначає глибину за дефісами й зберігає поточний шлях у стеку.
def recoverFromPreorder(traversal: str):
    root = None
    path = []
    for match in re.finditer(r"(-*)([0-9]+)", traversal):
        depth = len(match[1])
        node = TreeNode(int(match[2]))

        while len(path) > depth:
            path.pop()

        if not path:
            root = node
        elif path[-1].left is None:
            path[-1].left = node
        else:
            path[-1].right = node
        path.append(node)

    return root


if __name__ == "__main__":
    assert tree_to_list(recoverFromPreorder("1-2--3--4-5--6--7")) == [1, 2, 5, 3, 4, 6, 7]
    assert tree_to_list(recoverFromPreorder("1-2--3---4-5--6---7")) == [1, 2, 5, 3, None, 6, None, 4, None, 7]
    assert tree_to_list(recoverFromPreorder("1-401--349---90--88")) == [1, 401, None, 349, 88, 90]
    print("OK")
