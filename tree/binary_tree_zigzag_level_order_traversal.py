# -*- coding: utf-8 -*-
"""
# Time: O(n)
# Space: O(n)

# For examples:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#  [3],
#  [20,9],
#  [15,7]
# ]

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def zigzagorder(self, root):
        if root is None:
            return
        
        result = []
        
        currentlevel = [root]
        level = 0
        while(currentlevel):
            nextlevel = []
            vals = []
            for node in currentlevel:
                vals.append(node.val)
                if (node.left):
                    nextlevel.append(node.left)
                if (node.right):
                    nextlevel.append(node.right)

            # zigzag                    
            if (level % 2 == 0):
                result.append(vals)
            else:
                result.append(vals[::-1])
                
            level += 1
            currentlevel = nextlevel
        
        return result
        
        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    res = Solution().zigzagorder(root)
    print res