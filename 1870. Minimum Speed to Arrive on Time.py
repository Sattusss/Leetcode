from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist) - 1:
            return -1
        
        l, r = 1, 10 ** 7
        
        while l < r:
            m = l + (r - l) // 2
            
            if self.canReach(dist, hour, m):
                r = m
            else:
                l = m + 1
        
        return l
    
    def canReach(self, dist: List[int], hour: float, speed: int) -> bool:
        total = 0
        
        for i in range(len(dist) - 1):
            total += (dist[i] + speed - 1) // speed
        
        total += dist[-1] / speed
        
        return total <= hour