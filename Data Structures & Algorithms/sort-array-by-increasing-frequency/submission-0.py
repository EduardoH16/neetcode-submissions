class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_map = defaultdict(int)
        freq_map = defaultdict(set)
        res = []

        for n in nums:
            num_map[n] += 1
        
        if len(num_map) != len(set(num_map.values())):
            for num, freq in num_map.items():
                for num2, freq2, in num_map.items():
                    if num == num2:
                        continue
                    if freq == freq2:
                        freq_map[freq].add(num)
                        freq_map[freq].add(num2)

        while num_map:
            min_num = 0
            min_freq = float("inf")
            for key, val in num_map.items():
                if val < min_freq:
                    min_num = key
                    min_freq = val

            if min_freq not in freq_map:
                del num_map[min_num]
                for _ in range(int(min_freq)):
                    res.append(min_num)
            else:
                while freq_map[min_freq]:
                    max_num = max(freq_map[min_freq])
                    for _ in range(int(min_freq)):
                        res.append(max_num)
                    freq_map[min_freq].remove(max_num)
                    del num_map[max_num]

        return res
