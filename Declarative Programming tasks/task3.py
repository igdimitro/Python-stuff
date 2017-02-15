class Node:

    def __init__(self, val, children=[]):
        self.value = val
        self.children = children

    def __str__(self):
        return str(self.value)

#          65
#        /   \
#       14    70
#     /   \     \
#   11     16   90
#  /  \    /   /  \
# 4    12 15  77   95
#                 /
#                92

n92 = Node(92)
n56 = Node(56)
n77 = Node(77)
n95 = Node(95, [n92, None])
n4 = Node(4)
n12 = Node(12)
n15 = Node(15)
n11 = Node(11, [n4, n12])
n16 = Node(16, [n15, None])
n90 = Node(90, [n77, n95])
n70 = Node(70, [None, n90])
n14 = Node(14, [n11, n16])
root = Node(65, [n14, n70])
tree = {root, n14, n70, n90, n16, n11, n15, n12, n4, n95, n77, n92}


def helper(node):
    res = [node]
    if node.children:
        if node.children[0] is not None:
            res.extend(helper(node.children[0]))
        if node.children[1] is not None:
            res.extend(helper(node.children[1]))
    return res


def get_left_subtree(tree):
    if tree.children:
        if tree.children[0] is not None:
            return helper(tree.children[0])
    return []


def get_right_subtree(tree):
    if tree.children:
        if tree.children[1] is not None:
            return helper(tree.children[1])
    return []


def is_BST(tree):
    return (all(map(lambda node: len(node.children) <= 2, tree)) and
            all(map(lambda node:
                    all(map(lambda child: node.value > child.value,
                            get_left_subtree(node))) and
                    all(map(lambda child: node.value <= child.value,
                            get_right_subtree(node))), tree)))

#          65
#        /   \
#       14    70
#     /   \     \
#   11     16   82
#  /  \    /   /  \
# 4    12 15  77   83
#            /    /
#           56   81
n81 = Node(81)
n56 = Node(56)
n77 = Node(77, [n56, None])
n83 = Node(83, [n81, None])
n4 = Node(4)
n12 = Node(12)
n15 = Node(15)
n11 = Node(11, [n4, n12])
n16 = Node(16, [n15, None])
n82 = Node(82, [n77, n83])
n70 = Node(70, [None, n82])
n14 = Node(14, [n11, n16])
root = Node(65, [n14, n70])
tree2 = {root, n14, n70, n82, n16, n11, n15, n12, n4, n83, n77, n56, n81}


if __name__ == "__main__":
    print(is_BST(tree))
    print(is_BST(tree2))
