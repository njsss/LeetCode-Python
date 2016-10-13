# Time: O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        l1: ListNode
        L2: listNode
        """

        carry = 0
        dummy = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = dummy

        while (p1 or p2):
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next

            carry = val / 10
            val = val % 10
            p3.next = ListNode(val)
            p3 = p3.next

        if (carry == 1):
            p3.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addtwonumbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)
    
