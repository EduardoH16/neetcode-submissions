class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset_set = set()

        def backtrack(i, subset):
            if i >= len(nums):
                subset_set.add(tuple(subset))
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)

            subset.pop()
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return [list(t) for t in subset_set]