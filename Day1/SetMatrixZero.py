# Given an m x n integer matrix matrix, if an element is 0,
# set its entire row and column to 0's, and return the matrix.
# You must do it in place.
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# link to the Problem https://leetcode.com/problems/set-matrix-zeroes/

#Expected TC: O(MN)
#SC : O(1)

#Solution Using sets
def setZeroes(matrix):

        row = set()
        col = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        if len(row) == 0:
            return

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if i in row :
                    matrix[i][j] = 0
                elif j in col:
                    matrix[i][j] = 0



if __name__ == "__main__":
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        setZeroes(matrix)
        for i in range (len(matrix)):
            print(matrix[i])






