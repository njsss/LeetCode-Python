# -*- coding: utf-8 -*-
"""
# Time:  O(n)
# Space: O(1)

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

       1
      / \
     2   3
    / \
   4   5
return [1,2,4,5,3]

"""

class TreeNode:
    """
    Tree Node
    val: current value (any)
    left: left node (TreeNode)
    right: right node (TreeNode)
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    stack
    """
    def __init__(self):
        self.stack = [] # temperary store
        self.result = [] # return a list of val
        
    def preodertraversal(self, root):
        self.stack.append(root)
        
        while(self.stack):
            cur = self.stack.pop()
            self.result.append(cur.val)
            
            if (cur.right):
                self.stack.append(cur.right)
                
            if (cur.left):
                self.stack.append(cur.left)
        
        return self.result
        

if __name__ == "__main__":        
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    res = Solution().preodertraversal(root)
    print res
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    res = Solution().preodertraversal(root)
    
    print res