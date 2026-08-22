# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        mergedList = []

        for i in range(len(lists)):
            current = lists[i]
            while current:
                mergedList.append(current.val)
                current = current.next
        mergedList = sorted(mergedList)
        if mergedList:
            head = ListNode(mergedList[0])
        else:
            head = None   
        current = head
        
        for i in range(1,len(mergedList)):           
            current.next = ListNode(mergedList[i])
            current = current.next

        return head
'''
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        current = []
        for i in range(len(lists)):
            current.append(lists[i])
        
        result = []

        while any(current):

            for i in range(len(current)):
                if current[i] is not None:
                    minimum = current[i].val
                    index = i
                    break

            for i in range(len(current)):
                if current[i] is not None and current[i].val < minimum:
                    minimum = current[i].val
                    index = i           

            result.append(minimum)
            current[index] = current[index].next

        if result:
            head = ListNode(result[0])
        else:
            head = None

        current = head

        for i in range(1, len(result)):
            current.next = ListNode(result[i])
            current = current.next

        return head
'''

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))


        return dummy.next