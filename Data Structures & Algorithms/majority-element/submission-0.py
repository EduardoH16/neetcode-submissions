class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)

        for n in nums:
            freq_map[n] += 1
        
        for key, val in freq_map.items():
            if val > len(nums) / 2:
                return key