class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
    
    def prepend(self, value=-1):
        try:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
                return 0
            new_node.next = self.head
            self.head = new_node
            return 0
        except Exception as e:
            print("Unexpected error occured: {e}".format(e=e))
            return 1
        
    
    def append(self, value=-1):
        try:
            new_node = Node(value)
            if not self.head: # 0 nodes
                self.head = new_node
            else:
                curr = self.head
                while curr.next != None:
                    curr = curr.next
                curr.next = new_node
            return 0
        except Exception as e:
            print("Unexpected error occured: {e}".format(e=e))
            return 1
    
    def getLength(self):
        curr = self.head
        res = 0
        while curr != None:
            res += 1
            curr = curr.next
        return res
    
    def print_all_nodes (self):
        curr = self.head
        cnt = 1
        while curr != None:
            print("Node {cnt}: {value}".format(cnt=cnt, value=curr.value))
            curr = curr.next
            cnt += 1

if __name__ == "__main__":
    new_values = [3,5,8,6,9,1,0]
    ll = LinkedList()
    for value in new_values:
        ll.prepend(value)
    ll.print_all_nodes()
        