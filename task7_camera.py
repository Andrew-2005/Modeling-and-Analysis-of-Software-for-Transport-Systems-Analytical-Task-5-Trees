from tree_utils import build_tree, iter_postorder


# Ставить камеру у вузлі, якщо хоча б одна його дитина ще не покрита.
def minCameraCover(root):
    needs_camera, has_camera, covered = range(3)
    states = {}
    cameras = 0

    for node in iter_postorder(root):
        left = states.pop(node.left, covered)
        right = states.pop(node.right, covered)
        if needs_camera in (left, right):
            states[node] = has_camera
            cameras += 1
        elif has_camera in (left, right):
            states[node] = covered
        else:
            states[node] = needs_camera

    if states.get(root) == needs_camera:
        cameras += 1
    return cameras


if __name__ == "__main__":
    assert minCameraCover(build_tree([0, 0, None, 0, 0])) == 1
    assert minCameraCover(build_tree([0, 0, None, 0, None, 0, None, None, 0])) == 2
    print("OK")
