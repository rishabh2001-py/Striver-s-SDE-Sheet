# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#         1
#        1,1
#       1,2,1
#      1,3,3,1
#     1,4,6,4,1

# Example:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

#Problem Link : https://leetcode.com/problems/pascals-triangle/


def generate(numRows):
        dp =[]
        for i in range(0,numRows):
            arr = []
            for j in range(i+1):

                if j == 0 or j == i:
                    arr.append(1)
                else:
                    data = dp[i-1][j-1] + dp[i-1][j]
                    arr.append(data)
                    # print(data)
            dp.append(arr)
            arr= []


        return(dp)

if __name__ == "__main__":
    numRows = int(input("Enter Number of rows: "))
    ans = generate(numRows)
    for i in range(len(ans)):
        print(ans[i])



















