import json

from tree_utils import build_tree, tree_to_list


# Записує список рівнів дерева у форматі JSON.
def serialize(root):
    return json.dumps(tree_to_list(root), separators=(",", ":"))


# Відновлює дерево зі списку рівнів у JSON.
def deserialize(data):
    return build_tree(json.loads(data))


if __name__ == "__main__":
    for values in ([1, 2, 3, None, None, 4, 5], []):
        assert tree_to_list(deserialize(serialize(build_tree(values)))) == values
    print("OK")
