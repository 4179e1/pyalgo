#!/usr/bin/env python3


def min_tree_depth(root):
    if root is None:
        return 0

    depth = 1

    queue = [root]

    while len(queue) > 0:

        size = len(queue)
        for i in range(size):
            node = queue.pop(0)

            if (node["left"] == None) and (node["right"] == None):
                return depth 

            if node["left"] != None:
                queue.append(node["left"])
            if node["left"] != None:
                queue.append(node["left"])

        depth+=1

    return depth