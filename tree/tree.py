class BinaryTreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    
    def array_to_tree(arr):
        """
        [1,2,3,4,5,6,7 ]

        Args:
            arr (_type_): _description_
        """