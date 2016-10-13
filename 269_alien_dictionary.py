# Time: O(n)
# Space: O(|V| + |E|) = O(26 + 26^2) = O(1)
# There is a new alien language which uses the latin alphabet. However, the order
# among letters are unknown to you. You receive a list of words from the dictionary,
# where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
# For example,
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
#
# Note:
#
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# BFS Solution.
import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = []
        zero_in_degree_queue = collections.deque() # Returns a new deque object initialized left-to-right
        in_degree = {}
        out_degree = {}
        nodes = sets.Set()
        for word in words:
            for c in word:
                nodes.add(c)

        for i in range(1, len(words)):
            self.findEdges(word[i-1], words[i], in_degree, out_degree)

        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)

        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            result.append(precedence)

            if precedence in out_degree:
                for c in out-degree[precedence]:
                    indegree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)
                del out_degree[precedence]

        if out_degree:
            return ""

        return "".join(result)


        # Construct the Graph
        def findEdges(self, word1, word2, in_degree, out_degree):
            str_len = min(len(word1), len(word2))
            for in in range(str_len):
                if (word1[i] != word2[i]):
                    if word2[i] not in_degree:
                        in_degree[word2[i]] = sets.Set()
