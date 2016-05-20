# -*- coding: utf-8 -*-
"""
# Return the new root.
# 
# For example:
# Given a binary tree {1,2,3,4,5},
# 
#     1
#    / \
#   2   3
#  / \
# 4   5
# 
# return the root of the binary tree [4,5,2,#,#,3,1].
# 
#    4
#   / \
#  5   2
#     / \
#    3   1  
#
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def upsidedown(self, root):

        return self.upsidedownhelper(root, None)
        
    def upsidedownhelper(self, p, parent):
        if p is None:
            return parent
            
        root = self.upsidedownhelper(p.left, p)
         
        if parent:
            p.left = parent.right
        else:
            p.left = None
        p.right = parent
               
        return root
        

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    root = Solution().upsidedown(root)
