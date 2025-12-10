class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def list_to_tree_recursive(self, arr):
        n = len(arr)

        def add_to_tree(arr, i, n):
            currNode = None
            if i < n:
                currNode = TreeNode(arr[i])
                currNode.left = add_to_tree(arr, 2 * i + 1, n)
                currNode.right = add_to_tree(arr, 2 * i + 2, n)
            return currNode

        self.root = add_to_tree(arr, 0, n)
        return self.root

    def list_to_tree_iterative(self, arr):
        if not arr:
            return None
        q = []
        i = 1
        n = len(arr)
        root = TreeNode(arr[0])
        q.append(root)
        while i < n:
            currNode = q.pop(0)
            if i < n:
                currNode.left = TreeNode(arr[i])
                i += 1
                q.append(currNode.left)
            if i < n:
                currNode.right = TreeNode(arr[i])
                i += 1
                q.append(currNode.right)
        self.root = root
        return self.root

    def inorder_traversal(self, fn):
        def inorder_helper(node):
            if node:
                inorder_helper(node.left)
                fn(node)
                inorder_helper(node.right)

        inorder_helper(self.root)
        return

    def preorder_traversal(self, fn):
        def preorder_helper(node):
            if node:
                fn(node)
                preorder_helper(node.left)
                preorder_helper(node.right)

        preorder_helper(self.root)
        return

    def postorder_traversal(self, fn):
        def postorder_helper(node):
            if node:
                postorder_helper(node.left)
                postorder_helper(node.right)
                fn(node)

        postorder_helper(self.root)
        return

    def print_tree(self, order):
        def print_node(node):
            print(
                f"value: {node.value}, left: {node.left.value if node.left else 'None'}, right: {node.right.value if node.right else 'None'}"
            )

        if order == " in":
            self.inorder_traversal(print_node)
        elif order == "pre":
            self.preorder_traversal(print_node)
        elif order == "post":
            self.postorder_traversal(print_node)
        else:
            raise Exception("Unknown order.")


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    bitree = BinaryTree()
    bitree.list_to_tree_iterative(arr1)
