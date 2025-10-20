from linkedlist import Node, LinkedList

def getValueLL(ll):
    curr = ll.head
    res = ""
    while curr != None:
        res += str(curr.value)
        curr = curr.next
    return res

def reverseLL(ll):
    curr = ll.head
    prev = None
    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    ll.head = prev
    return
        

def checkPalindrome(ll):
    forwardStr = getValueLL(ll)
    reverseLL(ll)
    backwardStr = getValueLL(ll)
    return forwardStr == backwardStr

def checkPalindromeRunner(ll):
    slow = ll.head
    fast = ll.head
    st = []
    while fast and fast.next:
        st.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    # middle node
    if fast:
        slow = slow.next #skip because odd number: acbca, skip b
    while st:
        val = st.pop()
        if slow.value != val:
            return False
        slow = slow.next
    return True

class Result:
    def __init__(self, node=None, result=True):
        self.node = node
        self.result = result

def checkPalindromeRecursive(ll):
    len = ll.getLength()
    res = recurseHelper(ll.head, len)
    return res.result

def recurseHelper(node, len):
    if not node or len <= 0:
        return Result(node, True)
    if len == 1:
        return Result(node.next, True) 
    res = recurseHelper(node.next, len - 2)
    if not res.result or not res.node:
        return res
    res.result = node.value == res.node.value
    res.node = res.node.next
    return res
    
if __name__ == "__main__":
    new_values = list("abc")
    ll = LinkedList()
    for value in new_values:
        ll.append(value)
    ll.print_all_nodes()
    isPal = checkPalindromeRecursive(ll)
    print("==Reversed==")
    ll.print_all_nodes()
    print(isPal)
    