class Solution:
    def __init__(self):
        self
    def searchInsert(self, nums, target):
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        
        return L
    
pr = Solution()
 
nums = [1,2,3,4,5]
 
print(pr.searchInsert(nums, 6))