# # ProblemLink :https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6
import sys
def main():

    def maxSubArray(nums):

            if len(nums) == 1:
                return nums[0]
            sum = -sys.maxsize
            tempsum = 0
            for i in range (len(nums)):

                tempsum+=nums[i]
                sum = max(tempsum,sum)
                if tempsum<0:
                    tempsum = 0

            return sum

    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

main()