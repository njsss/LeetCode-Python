# data structure design
# Time: O(min(n,h)), per operation
# Space: O(min(n,h))
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing
# only letters a-z or ..
# a . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#
##################
# !Graph:
#          root
#         /  / \
#        b  d   m
#       /  /   /
#      a  a   a
#     /  /   /
#    d  d   d
class TreeNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word):
        """
        :type word: string
        :rtype : void
        """
        curr = self.root
        for c in word:
            if (not c in curr.leaves):
                curr.leaves[c] = TreeNode()
            curr = curr.leaves[c]
        curr.is_string = True

    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, curr):
        print (word, start, curr.leaves.keys())
        if (start == len(word)):
            return curr.is_string
        if (word[start] in curr.leaves):
            return self.searchHelper(word, start+1, curr.leaves[word[start]])
        elif (word[start] == '.'):
            for c in curr.leaves:
                if (self.searchHelper(word, start+1, curr.leaves[c])):
                    return True

        return False

# your WordDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print (wordDictionary.search("d.d"))
