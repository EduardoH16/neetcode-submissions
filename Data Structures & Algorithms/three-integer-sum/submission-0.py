class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            complement = -nums[i]
            while l < r:
                sum = nums[l] + nums[r]
                if sum == complement:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
                elif sum > complement:
                    r-=1
                else:
                    l+=1
        return res
                
               
