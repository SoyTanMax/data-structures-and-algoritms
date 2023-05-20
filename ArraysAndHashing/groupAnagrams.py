# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution(object):
    def groupAnagrams(self, strs):
        dictionary = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in dictionary:
                dictionary[sorted_string] = [string]
            else:
                dictionary[sorted_string].append(string)
        return dictionary.values()
