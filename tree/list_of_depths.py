from linkedlist import LinkedList
from binary_tree import BinaryTree
import random


def get_ll_depths(bintree):
    """Return list of head of linked list at each depth. Use queue for Breadth first search
    Args:
        bintree (_type_): root of binary tree
    Return:
        list
    """
    res = []
    root = bintree.root
    q = [root]
    nq = []
    d = 0
    while q or nq:
        while q:
            curr = q.pop(0)
            if len(res) <= d:
                new_ll = LinkedList()
                new_ll.append(curr.value)
                res.append(new_ll)
            else:
                res[d].append(curr.value)
            if curr.left:
                nq.append(curr.left)
            if curr.right:
                nq.append(curr.right)
        q = nq
        nq = []
        d += 1
    return res


if __name__ == "__main__":
    N = 10
    arr1 = [random.randint(1, 9) for _ in range(N)]
    print(arr1)
    bitree = BinaryTree()
    bitree.list_to_tree_iterative(arr1)
    # print("--Tree--")
    # bitree.print_tree("pre")
    # print()
    print("--LinkedList--")
    ll_depths = get_ll_depths(bitree)
    for ll in ll_depths:
        ll.print_all_nodes()
