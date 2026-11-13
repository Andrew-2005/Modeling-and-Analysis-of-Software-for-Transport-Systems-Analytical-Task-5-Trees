from tree_utils import build_tree


# Перевіряє пари вузлів на дзеркальних позиціях.
def isSymmetric(root):
    if root is None:
        return True

    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()
        if left is None or right is None:
            if left is not right:
                return False
            continue

        if left.val != right.val:
            return False
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))
    return True


if __name__ == "__main__":
    assert isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])) is True
    assert isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])) is False
    print("OK")
