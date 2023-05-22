# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

class Solution(object):
    def topKFrequent(self, nums, k):
        dictionary = {}
        frequency = [[] for n in range(len(nums) + 1)]

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

        for num, c in dictionary.items():
            frequency[c].append(num)

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]: 
                result.append(n)
                if len(result) == k:
                    return result