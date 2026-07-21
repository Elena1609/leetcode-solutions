class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val
    

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
        self.size+=1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return                                  
        else:  
            current = self.head
            for i in range(index-1):
                current = current.next       
            newNode = Node(val)
            newNode.next = current.next
            current.next = newNode
            
            self.size+=1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        current = self.head
        if index >= self.size or index < 0:
            return
        elif index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None                     
        else:    
            for i in range(index-1):
                current = current.next         
            current.next = current.next.next
            if index == self.size - 1:
                self.tail = current
                
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)