class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1 2 3 , 4 5 6 , 7 8 9
        # 1 4 7 , 2 5 6 , 3 8 9
        # 7 4 1 , 2 5 6 , 3 8 9
        # 7 4 1 , 2 5 8 , 3 6 9
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            matrix[i].reverse()