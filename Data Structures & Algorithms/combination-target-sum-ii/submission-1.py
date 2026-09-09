class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, sum, currList):
            if sum == target:
                res.append(currList.copy())
                return
            
            if i >= len(candidates) or sum > target:
                return
        
            currList.append(candidates[i])
            dfs(i + 1, sum + candidates[i], currList)
            
            currList.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sum, currList)
        
        dfs(0, 0, [])
        return res