class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charToIndex = {}
        start = 0
        maxLength = 0
        for i, char in enumerate(s):
            if char in charToIndex and charToIndex[char] >= start:
                start = charToIndex[char] + 1
            charToIndex[char] = i
            maxLength = max(maxLength, i - start + 1)
        return maxLength