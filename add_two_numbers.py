# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        [2,4,3]
        [5,6,4]


        math: 7 -> 10 -> 7
        sum:  7 -> 0  -> 7
        bag:  0 -> 1  -> 0


        beginNode = ListNode()

        crnt = beginNode - новый связанный список

        time: O(n)
        space: O(n)
        '''

        bag = 0
        sum = 0
        beginNode = ListNode()
        crnt = beginNode
        #times = 0
        while l1 or l2 or bag:

            '''
            [2,4,5,0,0,0,0,0,0,1]
            [5,6,4]
            '''
            if (not l1 or not l2) and not bag:
                crnt.next = l1 or l2
                break

            sum = bag
            #times +=1

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            bag = sum // 10

            crnt.next = ListNode(sum % 10)
            crnt = crnt.next
        # print(times)
        return beginNode.next
