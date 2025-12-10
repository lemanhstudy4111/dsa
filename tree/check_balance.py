from binary_tree import TreeNode, BinaryTree


def check_balance(bt):
    def check_balance_helper(node):
        if not node:
            return (0, True)
        # leaf
        if not node.left or not node.right:
            return (0, True)
        left_d = check_balance_helper(node)
        right_d = check_balance_helper(node)
        if not left_d[1] or not right_d[1]:
            return -1, False
        if left_d[0] + 1 > right_d[0] + 2:
            return -1, False
        return (max(left_d + 1, right_d + 1), True)

    return check_balance_helper(bt.root)[1]
