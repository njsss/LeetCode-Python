# -*- coding: utf-8 -*-
"""
Time: O(n)
Space: O(1)

Given binary tree [1,..., 2, 3],
   1
    \
     2
    /
   3
return [1,3,2]

       1
      / \
     2   3
    / \
   4   5
return [4,2,5,1,3]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution:
    # stack
    # root: a tree node
    # return a list of integers
    def inordertranversal(self, root):
        """
        root: TreeNode
        """
        result = []
        stack = []
        cur = root
        
        while (stack or cur):
            if (cur):
                stack.append(cur)
                cur = cur.left
            else:
                last = stack.pop()
                result.append(last.val)
                cur = last.right
                
        return result
        

class Solution2:
    # recursive
    def __init__(self):
        self.result = []
    
    def inordertranversal(self, root):
        if (root):
            self.rec(root)
        
        return self.result
        
    def rec(self, node):
        if (node.left):
            self.rec(node.left)
        
        self.result.append(node.val)
        
        if (node.right):
            self.rec(node.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    res1 = Solution().inordertranversal(root)
    res2 = Solution2().inordertranversal(root)
    
    print res1
    print res2