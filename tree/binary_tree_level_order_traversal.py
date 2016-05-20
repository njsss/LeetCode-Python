# -*- coding: utf-8 -*-
"""
# Time: O(n)
# Space: O(h)
#
# Given a binary tree, return the level order traversal of its nodes' values
# (ie, from left to right, level by level).

# For example:
# Given binary tree {3, 9, 20, #, #, 15, 7},
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its leve order traversal as [[3],[9,20],[15,7]]

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def leveloder(self, root):
        if root is None:
            return []

        result = []
        
        currentlevel = []       
        currentlevel.append(root)
        while (currentlevel):
            vals = []
            nextlevel = []
            for node in currentlevel:
                vals.append(node.val)
                if (node.left):
                    nextlevel.append(node.left)
                if (node.right):
                    nextlevel.append(node.right)
            
            currentlevel = nextlevel
            result.append(vals)
            
        return result
        

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    res = Solution().leveloder(root)
    print res
    # for reverse order
    res.reverse()
    print res