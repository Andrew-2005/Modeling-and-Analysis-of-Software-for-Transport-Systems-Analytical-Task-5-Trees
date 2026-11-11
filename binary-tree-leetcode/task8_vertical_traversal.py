from itertools import groupby
from operator import itemgetter

from tree_utils import build_tree


# Сортує вузли за стовпцем, рядком і значенням та групує за стовпцем.
def verticalTraversal(root):
    positions = []
    stack = [(root, 0, 0)] if root is not None else []
    while stack:
        node, row, column = stack.pop()
        positions.append((column, row, node.val))
        if node.left is not None:
            stack.append((node.left, row + 1, column - 1))
        if node.right is not None:
            stack.append((node.right, row + 1, column + 1))

    positions.sort()
    return [[value for _, _, value in group] for _, group in groupby(positions, key=itemgetter(0))]


if __name__ == "__main__":
    assert verticalTraversal(build_tree([3, 9, 20, None, None, 15, 7])) == [[9], [3, 15], [20], [7]]
    assert verticalTraversal(build_tree([1, 2, 3, 4, 5, 6, 7])) == [[4], [2], [1, 5, 6], [3], [7]]
    assert verticalTraversal(build_tree([1, 2, 3, 4, 6, 5, 7])) == [[4], [2], [1, 5, 6], [3], [7]]
    print("OK")
