class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()

        for n in nums:
            seen.add(n)
        
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res.append(i)
            
        return res