# -*- coding: utf-8 -*-
"""
Created on Tue May 03 22:56:05 2016

@author: SSS
"""

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution(object):
    def addtwonumbers(self, l1, l2):
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