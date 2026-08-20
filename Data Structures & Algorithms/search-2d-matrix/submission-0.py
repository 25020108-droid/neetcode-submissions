class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        n = len(matrix)
        m = len(matrix[0])
        right = n*m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // m][mid % m] == target:
                return True
            elif matrix[mid // m][mid % m] > target:
                right = mid - 1
            elif matrix[mid // m][mid % m] < target:
                left = mid + 1
        return False

        

        