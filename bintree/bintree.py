
def new_tree_node (value):
    return {
        "value": value,
        "left": None,
        "right": None,
    }

def tree_from_list (l):
    if (len(l) == 0):
        return None


    root = new_tree_node(l[0])
    queue = [root]
    parent = []

    for item in l:
        node = queue.pop(0)

        if item == None:
            continue

        node["value"] = item

        node["left"] = new_tree_node(None)
        node["right"] = new_tree_node(None)

        # left
        queue.append (node["left"])
        # right
        queue.append (node["right"])


    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        if node["left"]["value"] == None:
            node["left"] = None
        else:
            queue.append (node["left"])
        if node["right"]["value"] == None:
            node["right"] = None
        else:
            queue.append (node["right"])


    return root


if __name__ == "__main__":
    tree = tree_from_list ([3, 9, 20, None, None, 15, 7])

    from pprint import pprint
    pprint (tree)