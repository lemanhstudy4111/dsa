from binary_tree import TreeNode
import math


class BST:
    def __init__(self, root=None):
        self.root = root

    def inorder_traversal(self):
        def inorder_helper(node):
            if node:
                inorder_helper(node.left)
                print(
                    f"curr node: {node.value}, left: {node.left.value if node.left else 'None'}, right: {node.right.value if node.right else 'None'}"
                )
                inorder_helper(node.right)

        inorder_helper(self.root)
        return

    def preorder_traversal(self):
        def preorder_helper(node):
            if node:
                print(
                    f"curr node: {node.value}, left: {node.left.value if node.left else 'None'}, right: {node.right.value if node.right else 'None'}"
                )
                preorder_helper(node.left)
                preorder_helper(node.right)

        preorder_helper(self.root)
        return

    def postorder_traversal(self):
        def postorder_helper(node):
            if node:
                postorder_helper(node.left)
                postorder_helper(node.right)
                print(
                    f"curr node: {node.value}, left: {node.left.value if node.left else 'None'}, right: {node.right.value if node.right else 'None'}"
                )

        postorder_helper(self.root)
        return


def list_to_bst_recursive(list):
    def add_to_tree(start, end):
        if start > end:
            return None
        mid = math.floor((start + end) / 2)
        curr_node = TreeNode(list[mid])
        curr_node.left = add_to_tree(start, mid - 1)
        curr_node.right = add_to_tree(mid + 1, end)
        return curr_node

    new_tree = BST()
    new_tree.root = add_to_tree(0, len(list) - 1)
    return new_tree


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6]
    bitree = list_to_bst_recursive(arr1)
    bitree.preorder_traversal()
