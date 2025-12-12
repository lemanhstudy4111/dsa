import random
from binary_tree import TreeNode, BinaryTree


def check_balance(bt):
    def check_balance_helper(node):
        if not node:
            return (0, True)
        # leaf
        if not node.left or not node.right:
            return (0, True)
        left_d = check_balance_helper(node.left)
        right_d = check_balance_helper(node.right)
        if not left_d[1] or not right_d[1]:
            return (-1, False)
        if left_d[0] + 1 > right_d[0] + 2:
            return (-1, False)
        val = max(left_d[0] + 1, right_d[0] + 1)
        return (val, True)

    return check_balance_helper(bt.root)[1]


class TestClass:
    def test_balance(self):
        N = 10
        arr1 = [random.randint(1, 9) for _ in range(N)]
        print(arr1)
        bitree = BinaryTree()
        bitree.list_to_tree_iterative(arr1)
        assert check_balance(bitree)
