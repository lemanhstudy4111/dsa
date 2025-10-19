from linkedlist import Node, LinkedList

def partition(ll, target):
    print("==Partitioned==")
    curr = ll.head
    last_smaller = Node(-1, ll.head) #dummy node
    prev = last_smaller
    while curr != None:
        if curr.value < target:
            prev.next = curr.next
            next_node = last_smaller.next
            last_smaller.next = curr
            curr.next = next_node
            if next_node == ll.head:
                ll.head = curr
            last_smaller = curr
        prev = curr
        curr = curr.next
    return

if __name__ == "__main__":
    new_values = [2,5,1,6,3,7]
    ll = LinkedList()
    for value in new_values:
        ll.append(value)
    ll.print_all_nodes()
    partition(ll, 5)
    ll.print_all_nodes()