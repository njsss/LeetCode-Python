# -*- coding: utf-8 -*-
"""
# Time:  O(n)
# Space: O(h)
#
# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  /
# 6               <---
# You should return [1, 3, 4, 6].
#
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def rightsideview(self, root):
        result = []
        if not root:
            return result
            
        self.rightsideviewhelper(root, 1, result)
        return result

    def rightsideviewhelper(self, node, depth, result):
        if (not node):
            return
            
        if (depth > len(result)):
            result.append(node.val)
        
        self.rightsideviewhelper(node.right, depth+1, result)
        self.rightsideviewhelper(node.left, depth+1, result)


class Solution2:
    def rightsideview(self, root):
        if root is None:
            return []
        
        result = []
        current = [root]
        
        while (current):
            nextlevel = []
            for i, node in enumerate(current):
                if (i == 0):
                    result.append(node.val)
                if (node.right):
                    nextlevel.append(node.right)
                if (node.left):
                    nextlevel.append(node.left)
            current = nextlevel
        
        return result
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    root.left.right.left = TreeNode(6)
    
    res = Solution().rightsideview(root)
    print res
    
    res = Solution2().rightsideview(root)
    print res