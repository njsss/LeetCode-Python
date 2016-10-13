# Time: O(1)
# Space: O(1)
#
# Given a non-negative integer num, repeatedly add
# all its digits until the result has only on e digit.
#
# For example
# givien num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2,
# since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
# Hint:
# A nativie implementation of the above process is trivial.
# Could you come up with other methods?
#
class Solution:
    def addDigits(self, num):
        """
        :type num :integer
        :rtype :integer
        """

        return (num-1) % 9 + 1 if num>0 else 0

class Solution2:
    def addDigits(self, num):
        """
        """
        if (num <= 9):
            return num

        val = 0
        while (num % 10 > 0):
            val += num % 10
            num = num / 10
        
        return (self.addDigits(val))


if __name__ == "__main__":
    result = Solution2().addDigits(338)
    print (result)
