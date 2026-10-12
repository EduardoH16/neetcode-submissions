class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = len(nums) + 1
        sum = 0

        while r < len(nums):
            sum += nums[r]
            while sum >= target and l <= r:
                res = min(res, r - l + 1)     
                sum -= nums[l]
                l += 1
            r += 1
        
        return res if res != len(nums) + 1 else 0