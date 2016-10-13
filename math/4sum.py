# Time: O(n^3)
# Space: O(1)

# Given an array S of n integers,
# are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.

# Note:
# Elements in a quaruplet (a,b,c,d) must be in non-descending order. (ie. a<=b<=c<=d)
# The solution set must not contain duplicate quadruplets.
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
# A solution set is:
#  (-1, 0, 0, 1)
#  (-2, -1, 1, 2)
#  (-2, 0, 0, 2)

import time

# Two pointer solution. (1356ms)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: [int]
        :type target: int
        :rtype: [[int]]
        """

        nums.sort()
        res = []

        for i in range(len(nums) -3):
            # avoid duplicate solution
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                # avoid duplicate solution
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j+1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res


# Time: O(n^2 * p)
# Space: O(n^2 * p)
# Hash Solution. (224ms)
import collections
class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: [int]
        :type target: int
        :rtype: [[int]]
        """

        nums = sorted(nums)
        result = []
        lookup = collections.defaultdict(list)
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                is_duplicated = False
                for [x,y] in lookup[nums[i] + nums[j]]:
                    if (nums[x] == nums[i]):
                        is_duplicated = True
                        break
                if (not is_duplicated):
                    lookup[nums[i] + nums[j]].append([i,j])

        ans = {}
        for c in range(2, len(nums)):
            for d in range(c+1, len(nums)):
                if ((target - nums[c] - nums[d]) in lookup):
                    for [a,b] in lookup[target - nums[c] - nums[d]]:
                        if b < c:
                            quad = [nums[a], nums[b], nums[c], nums[d]]
                            quad_hash = " ".join(str(quad))
                            if quad_hash not in ans:
                                ans[quad_hash] = True
                                result.append(quad)

        return result


class Solution3(object):
    def fourSum(self, nums, target):
        """
        """
        nums = sorted(nums)
        result = []
        lut = {}

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                k = j + 1
                l = len(nums) - 1

                while (k < l):
                    s = nums[i] + nums[j] + nums[k] + nums[l]

                    if (s > target):
                        l -= 1
                    elif (s < target):
                        k += 1
                    else:
                        quad = [nums[i], nums[j], nums[k], nums[l]]
                        quad_hash = " ".join(str(quad))
                        if (quad_hash not in lut):
                            lut[quad_hash] = True
                            result.append(quad)

                        k += 1
                        l -= 1

        return result


if __name__ == '__main__':
    start = time.time()
    result = Solution3().fourSum([1,0,-1,0,-2,2],0)
    end = time.time()
    print (result)
    print (end - start)*1000
