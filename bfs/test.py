from pprint import pprint
def test_min_tree_depth():
    cases = [
        [],
        [1],
        [3, 9, None],
        [3, None, 20],
        [3, 9, 20, None, 21, 15, 7],
    ]

    heights = [
        0,
        1,
        2,
        2,
        3,
    ]

    from bintree import tree_from_list
    from mintreedepth import min_tree_depth

    for c, h in zip (cases, heights):
        tree = tree_from_list(c)
        got = min_tree_depth(tree)

        assert got == h
