class Solution:
    def can_eat(self, piles, h, speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division
        return hours <= h
    
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.can_eat(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return left
