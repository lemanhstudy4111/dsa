from linkedlist import Node, LinkedList

def storeRef(ll):
    curr = ll.head
    refs = set()
    while curr:
        refs.add(curr)
        curr = curr.next
    return refs

def checkIntersectSet(ll1, ll2):
    ref = storeRef(ll1)
    curr = ll2.head
    while curr:
        if curr in ref:
            return curr
        curr = curr.next
    return None

def getTailAndSize(ll):
    curr = ll.head
    prev = None
    len = 0
    while curr:
        len += 1
        prev = curr
        curr = curr.next
    return len, prev

def checkIntersectPtr(ll1, ll2):
    len1, tail1 = getTailAndSize(ll1)
    len2, tail2 = getTailAndSize(ll2)
    if tail1 != tail2:
        return None
    longer_head = shorter_head = None
    if len1 > len2:
        longer_head = ll1.head
        shorter_head = ll2.head
    else:
        longer_head = ll2.head
        shorter_head = ll1.head
    num_skip = abs(len1 - len2)
    for _ in range(num_skip):
        longer_head = longer_head.next
    print(f"longer {longer_head}, shorter {shorter_head}")
    while shorter_head:
        if longer_head == shorter_head:
            return shorter_head
        longer_head = longer_head.next
        shorter_head = shorter_head.next
    return None

if __name__ == "__main__":
    new_values = [3,5,8,6,9,1,0]
    ll1 = LinkedList()
    for value in new_values:
        ll1.append(value)
    ll1.print_all_nodes()
    ll2 = LinkedList(Node(6, Node(8, Node(9, None))))
    ll2.print_all_nodes()
    res = checkIntersectPtr(ll1, ll2)
    print(res)
    