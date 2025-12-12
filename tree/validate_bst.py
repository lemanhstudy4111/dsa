from bst import BST
from binary_tree import TreeNode, BinaryTree


def check_bst(bitree):
    def check_bst_helper(node):
        if not node:
            return (float("-inf"), True)
        left_val = check_bst_helper(node.left)
        right_val = check_bst_helper(node.right)
        if not left_val[1] or not right_val[1]:
            return (-1, False)
        if (
            left_val[0] > node.val
            or left_val[0] != node.val
            or node.val > right_val[0]
        ):
            return (-1, False)
        return (max(left_val, right_val), True)

    return check_bst_helper(bitree.root)[1]


class TestClass:
    def test_bst(self):
        
