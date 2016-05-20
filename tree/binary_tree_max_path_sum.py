# -*- coding: utf-8 -*-
"""
# Time: O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    maxsum = float("-inf")
    def maxpathsum(self, root):
        self.maxpathsumhelper(root)
        
        return self.maxsum
        
    def maxpathsumhelper(self, root):
        if not root:
            return 0
            
        left = self.maxpathsumhelper(root.left)
        right = self.maxpathsumhelper(root.right)
        
        self.maxsum = max(self.maxsum, root.val + left + right)
        
        return root.val + max(left, right)
        

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = Solution().maxpathsum(root)
    
    print res