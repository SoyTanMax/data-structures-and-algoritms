# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 
# Input: nums = [1,2,3,1]
# Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for i, num in enumerate(nums): 
            if num in seen:
                return True
            else: 
                seen[num] = num
        return False