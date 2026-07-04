class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l, r = 0, len(matrix[row]) - 1
            if target < matrix[row][l] or target > matrix[row][r]:
                continue 
            while l <= r:
                mid = l + ((r-l) // 2)
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False
                    

        