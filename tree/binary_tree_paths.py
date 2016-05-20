# -*- coding: utf-8 -*-
"""
# Time:  O(n * h)
# Space: O(h)
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def binarytreepaths(self, root):
        result = []
        path = []
        
        if (root is None):
            return result
            
#        path.append(str(root.val))
        self.binarytreepathshelper(root, path, result)
        
        return result
        
    def binarytreepathshelper(self, root, path, result):      
        if (not root):
            return

        path.append(str(root.val))
                
        if (root.left is None and root.right is None):
            result.append("->".join(path))
            path.pop()
            return
            
        if (root.left):
            self.binarytreepathshelper(root.left, path, result)
            
        if (root.right):
            self.binarytreepathshelper(root.right, path, result)
            
        path.pop()
            

           
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    
    res = Solution().binarytreepaths(root)
    print res