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
        q = []
        i = 0
        n = len(arr)
        root = TreeNode(arr[i])
        q.append(root)
        while i < n:
            currVal = q.pop()
            currNode = TreeNode(currVal)
            if i < n:
                i += 1
                currNode.left = TreeNode(arr[i])
                q.append(currNode.left)
            if i < n:
                i += 1
                currNode.right = TreeNode(arr[i])
                q.append(currNode.right)
        self.root = root
        return self.root

    def inorder_traversal(self):
        def inorder_helper(node):
            if node:
                inorder_helper(node.left)
                print()


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
