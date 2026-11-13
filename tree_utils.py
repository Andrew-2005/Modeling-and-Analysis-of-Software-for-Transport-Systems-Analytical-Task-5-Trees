from collections import deque


class TreeNode:
    # Зберігає значення вузла та посилання на його дітей.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Читає пари дітей для наявних батьків у порядку рівнів.
def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    parents = deque([root])
    remaining = iter(values)
    next(remaining)

    while parents:
        parent = parents.popleft()
        left = next(remaining, None)
        right = next(remaining, None)
        if left is not None:
            parent.left = TreeNode(left)
            parents.append(parent.left)
        if right is not None:
            parent.right = TreeNode(right)
            parents.append(parent.right)

    return root


# Записує вузли по рівнях і видаляє кінцеві пропуски.
def tree_to_list(root):
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node.val)
            queue.extend((node.left, node.right))

    while values and values[-1] is None:
        values.pop()
    return values


# Повертає кожен вузол після його дітей за допомогою стека.
def iter_postorder(root):
    stack = [(root, False)] if root is not None else []
    while stack:
        node, expanded = stack.pop()
        if expanded:
            yield node
            continue

        stack.append((node, True))
        if node.right is not None:
            stack.append((node.right, False))
        if node.left is not None:
            stack.append((node.left, False))


if __name__ == "__main__":
    assert tree_to_list(build_tree([])) == []
    assert tree_to_list(build_tree([1, None, 2, 3, None])) == [1, None, 2, 3]
    assert [node.val for node in iter_postorder(build_tree([1, 2, 3]))] == [2, 3, 1]
    print("OK")
