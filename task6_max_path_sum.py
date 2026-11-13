from tree_utils import build_tree, iter_postorder


# Для кожного вузла обчислює найкращу гілку та шлях через нього.
def maxPathSum(root):
    gains = {}
    best = float("-inf")
    for node in iter_postorder(root):
        left_gain = max(0, gains.pop(node.left, 0))
        right_gain = max(0, gains.pop(node.right, 0))
        best = max(best, node.val + left_gain + right_gain)
        gains[node] = node.val + max(left_gain, right_gain)
    return best


if __name__ == "__main__":
    assert maxPathSum(build_tree([1, 2, 3])) == 6
    assert maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42
    print("OK")
