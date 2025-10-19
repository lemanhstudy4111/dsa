from linkedlist import Node, LinkedList

def removeDups(ll):
    """_summary_

    Args:
        ll (_type_): Linkedlist with duplicates
    
    store values in a frequency dictionary
    """
    freq = set()
    curr = ll.head
    prev = Node(None, next=curr) # dummy node
    while curr != None:
        if curr.value in freq:
            prev.next = curr.next
        else:
            freq.add(curr.value)
            prev = curr
        curr = curr.next
        

def removeDupsNoBuffer(ll):
    slow = ll.head
    fast = ll.head
    while slow != None and slow.next != None:
        while fast.next != None:
            if fast.next.value == slow.value:
                fast.next = fast.next.next
            else:
                fast = fast.next
        slow = slow.next
        fast = slow    
    return

if __name__ == "__main__":
    new_values = [3]
    ll = LinkedList()
    for value in new_values:
        ll.append(value)
    ll.print_all_nodes()
    removeDupsNoBuffer(ll)
    print("==Removed==")
    ll.print_all_nodes()