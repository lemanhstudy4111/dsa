from linkedlist import Node, LinkedList

def sumListsBackwards(ll1, ll2):
    bonus = 0
    res = LinkedList()
    curr = Node(-1, res.head)
    while ll1 and ll2:
        val = ll1.value + ll2.value + bonus
        print(val)
        bonus = val // 10
        if not res.head:
            res.head = Node(val % 10)
            curr = res.head
        else:
            curr.next = Node(val % 10)
            curr = curr.next
        ll1 = ll1.next
        ll2 = ll2.next
    while ll1:
        next_val = ll1.value + bonus
        bonus = next_val // 10
        curr.next = Node(next_val % 10)
        curr = curr.next
        ll1 = ll1.next
    while ll2:
        next_val = ll2.value + bonus
        bonus = next_val // 10
        curr.next = Node(next_val % 10)
        curr = curr.next
        ll2 = ll2.next
    if not ll1 and not ll2 and bonus > 0:
        curr.next = Node(bonus)
        curr = curr.next
    return res

def padLists(ll, num_zeros):
    for _ in range(num_zeros):
        ll.prepend(0)
    return ll
def sumListsHelper(n1, n2, res):
    if not n1 and not n2:
        return 0
    carry = sumListsHelper(n1.next, n2.next, res)
    value = carry + n1.value + n2.value
    res.prepend(value %  10)
    carry = value // 10
    return carry

def sumListsForward(ll1, ll2):
    len1 = ll1.getLength()
    len2 = ll2.getLength()
    if (len1 < len2):
        padLists(ll1, len2 - len1)
    else:
        padLists(ll2, len1 - len2)
    res_ll = LinkedList()
    last_carry = sumListsHelper(ll1.head, ll2.head, res_ll)
    if last_carry > 0:
        res_ll.prepend(last_carry)
    return res_ll
        

        
if __name__ == "__main__":
    new_values1 = [7,1,6]
    new_values2 = [5,9,2]
    ll1 = LinkedList()
    ll2 = LinkedList()
    for value in new_values1:
        ll1.append(value)
    for value in new_values2:
        ll2.append(value)
    res = sumListsForward(ll1, ll2)
    print("Summed")
    res.print_all_nodes()