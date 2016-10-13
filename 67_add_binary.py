# Time: O(n)
# Space: O(1)
#
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100"
#

class Solution:
    def addBinary(self, a, b):
        """
        :param a, string
        :param b, string
        :return, string
        """
        result = ""
        carry = 0
        val = 0

        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
                # val += int(a[len(a)-1-i])
            if i < len(b):
                val += int(b[-(i+1)])
                # val += int(b[len(b)-1-i])
            carry = val / 2
            val = val % 2
            result += str(val)
        if carry:
            result += str(carry)

        return result[::-1]

if __name__ == '__main__':
    result = Solution().addBinary('11','1')
    print (result)
