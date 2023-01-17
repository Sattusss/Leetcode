class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oneCount, flipCount = 0,0                 
        for c in s:
            if c == "1":
                oneCount += 1
            else:                                   
                if oneCount >= 1:       
                    flipCount += 1                   
            flipCount = min(flipCount, oneCount)    
        return flipCount