class Solution:
    def findDuplicate(self, nums: List[int]) -> int:        
        # linked list O(1)?
        # n = 4
        
        # -1, 3, -4, -2, 2 
        # nums[abs(nums[i]) - 1] *= -1
        # -1, -2, -3, 2, 2,
        # 2 1 2 3
        # -2 -1 
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
        
            
            