from linkedlist import Node, LinkedList


def findStartOfCycle(ll):
    slow = ll.head
    fast = ll.head
    while slow and fast and fast.next:
        if slow == fast and slow != ll.head:  # cycle
            slow = ll.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        slow = slow.next
        fast = fast.next.next
    return None


if __name__ == "__main__":
    new_values = [3, 5, 8, 6, 9, 1, 0]
    ll = LinkedList()
    for value in new_values:
        ll.append(value)
    curr = ll.head
    prev = None
    while curr:
        prev = curr
        curr = curr.next
    prev.next = ll.head.next.next.next
    circularStart = findStartOfCycle(ll)
    print(f"{circularStart.value}, {circularStart.next.value}")
