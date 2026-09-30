class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset_set = set()
        subset = []

        def dfs(i):
            if i >= len(nums):
                subset_set.add(tuple(subset))
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return [list(t) for t in subset_set]