# -*- coding: utf-8 -*-
"""
       1
      / \
     2   3
    / \
   4   5
      /
     6
return [4,6,5,2,3,1]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def __init__(self):
        self.stack = []
        self.result = []
        
    def postordertraversal(self, root):
        
        self.stack.append(root)
        cur = root
        
        while(self.stack):
            cur = self.stack[-1]

            if (not (cur.left or cur.right)):
                # this is leaf
                cur = self.stack.pop()
                self.result.append(cur.val)
                continue
            else:
                # this is node
                if (cur.right):
                    # push right child in stack
                    self.stack.append(cur.right)
                    # release parent hook
                    cur.right = None
                if (cur.left):
                    # push left left in stack
                    self.stack.append(cur.left)
                    # release parent hook
                    cur.left = None

        return self.result
        

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    
    res = Solution().postordertraversal(root)
    
    print res