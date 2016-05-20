# -*- coding: utf-8 -*-
"""
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
     \
      _25
      
[[4],[9],[3,5,2],[25,20],[7]]      
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def __init__(self):
        self.min = 0
        self.max = 0
        self.map = {}        
        
    def verticalorder(self, root):
        result = []
        
        self.verticalorderhelper(root, 0)
        
        level = range(self.min, self.max+1, 1)
        for l in level:
            result.append(self.map[l])
            
        return result
        
    def verticalorderhelper(self, node, level):
        if not node:
            return

        # create dictionary of list {,[]}
        if (level in self.map):
            self.map[level].append(node.val)
        else:
            self.map[level] = [node.val]
        
        cur = self.verticalorderhelper(node.left, level-1)
        if (cur is None):
            self.min = min(self.min, level)
            
        cur = self.verticalorderhelper(node.right, level+1)
        if (cur is None):
            self.max = max(self.max, level)

        return node
        

if __name__ == "__main__":
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(7)
        root.left.right.right = TreeNode(25)
        
        res = Solution().verticalorder(root)
        print res