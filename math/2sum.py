# -*- coding: utf-8 -*-
"""
# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
"""

class Solution(object):
    def twosum(self, nums, target):
        """
        ([int], int) --> [int]
        
        nums: list of numbers
        target: target of sum
        return: indices of two numbers
        
        >>> nums = [2, 7, 11, 15]
        >>> target = 9
        >>> twosum(nums, target)
        [0, 1]
        """
        lut = {}
        for i, num in enumerate(nums):
            if (target-num) in lut:
                return ([lut[target-num],i])
            lut[num] = i
        
        return []
        
if __name__ == "__main__":
    print Solution().twosum([2,7,11,15],9)
