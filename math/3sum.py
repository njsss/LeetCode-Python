#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Time: O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)
#

"""

class Solution:
    def threesum(self, nums):
        """
        nums: [int]
        """
        # sort array
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            # avoid duplicate solution
            if (i==0 or nums[i]>nums[i-1]):
                j = i + 1
                k = len(nums) - 1
                while (j < k):
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        print result
                        j = j + 1
                        k = k - 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1

        return result

if __name__ == '__main__':
    result = Solution().threesum([-1,0,1,2,-1,-4])
    # print result
