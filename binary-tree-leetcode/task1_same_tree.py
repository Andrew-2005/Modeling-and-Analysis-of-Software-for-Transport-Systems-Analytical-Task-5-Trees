from tree_utils import build_tree


# Порівнює значення й розташування відповідних вузлів.
def isSameTree(p, q):
    stack = [(p, q)]
    while stack:
        first, second = stack.pop()
        if first is None or second is None:
            if first is not second:
                return False
            continue

        if first.val != second.val:
            return False
        stack.append((first.left, second.left))
        stack.append((first.right, second.right))
    return True


if __name__ == "__main__":
    assert isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False
    print("OK")
