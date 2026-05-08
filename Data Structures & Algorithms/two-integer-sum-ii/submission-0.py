class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end:
            left = numbers[start]
            right = numbers[end]
            sum = left + right
            if sum == target:
                return [start+1, end+1]
            elif sum < target:
                start += 1
            else:
                end -= 1
            
            