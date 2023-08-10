class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def search(left: int, right: int) -> bool:
            if left > right:
                return False
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return search(left, mid - 1)
                else:
                    return search(mid + 1, right)
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    return search(mid + 1, right)
                else:
                    return search(left, mid - 1)
            else:
                return search(left + 1, right)
        return search(0, len(nums) - 1)