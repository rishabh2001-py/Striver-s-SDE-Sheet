
#Problem Link : https://leetcode.com/problems/find-the-duplicate-number/
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicate(nums):

        fast = nums[0]
        slow = nums[0]
        # sta = -1
        while(True):

            fast = nums[nums[fast]]
            slow = nums[slow]

            if nums[fast] == nums[slow]:
                break
        fast = nums[0]
        while(fast != slow):
            fast = nums[fast]
            slow = nums[slow]

        return fast

def main():
     arr = [1,3,4,3,2,5]
     print(findDuplicate(arr))

main()