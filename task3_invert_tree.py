from tree_utils import build_tree, tree_to_list


# Міняє місцями ліву й праву дитину кожного вузла.
def invertTree(root):
    stack = [root] if root is not None else []
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return root


if __name__ == "__main__":
    assert tree_to_list(invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(invertTree(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert tree_to_list(invertTree(build_tree([]))) == []
    print("OK")
