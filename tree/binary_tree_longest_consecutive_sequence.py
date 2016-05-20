# -*- coding: utf-8 -*-
"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node 
in the tree along the parent-child connections. The longest consecutive path 
need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.


"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution():
    def longestconsecutive(self, root):
        """
        """
        if (not root):
            return 0
            
        return self.longestconsecutivehelper(root, 0, root.val)
        
    def longestconsecutivehelper(self, root, curlen, preval):
        if (not root):
            return curlen
            
        if (root.val == preval + 1):
            curlen += 1
        else:
            curlen = 1
            
        leftlen = self.longestconsecutivehelper(root.left, curlen, root.val)
        rightlen = self.longestconsecutivehelper(root.right, curlen, root.val)
        
        return max(curlen, leftlen, rightlen)
            
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    
    res = Solution().longestconsecutive(root)
    print res
    
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(1)

    res = Solution().longestconsecutive(root)
    print res
    