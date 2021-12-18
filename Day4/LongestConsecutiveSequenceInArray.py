# Problem Link : https://leetcode.com/problems/longest-consecutive-sequence/
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

def longestConsecutive(nums):
    res = []
    s = set()

    for i in nums:
        s.add(i)

    for i in nums:

        if i - 1 not in s:
            element = i
            temp = []

            while (element in s):
                temp.append(element)
                element += 1

            if len(temp) > len(res):
                res = temp

    print(res)
    return len(res)


if __name__ == "__main__":
    arr = [3, 4, 1, 6, 7, 8, 9, 11, 7, 24, 21, 22, 67, 28, 23, 25, 26, 20]
    print(longestConsecutive(arr))
