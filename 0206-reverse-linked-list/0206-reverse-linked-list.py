# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution(object):
    def reverseList(self, head):
        #назначаем указатели для левой (пока пусто) и правой части (весь список)
        prev = None
        current = head

        while current is not None:        
            next_node = current.next #сохранение правой части
            current.next = prev #разворот стрелки влево для левой части
            # двигаем указатели
            prev = current
            current = next_node
        return prev
"""
class Solution(object):   

    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head