class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numToCount = {}
        for num in nums:
            numToCount[num] = numToCount.get(num, 0) + 1
        for num, count in numToCount.items():
            if count == 1:
                return num
        return -1