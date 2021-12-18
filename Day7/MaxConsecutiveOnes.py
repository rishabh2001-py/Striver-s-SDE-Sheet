
if __name__ == '__main__':
    def findMaxConsecutiveOnes(nums):


        max1s = 0
        i = 0
        while(i<len(nums)):

            if nums[i] == 1:
                curMax = 0
                while(i<len(nums) and nums[i]== 1):
                    curMax+=1
                    i+=1

                max1s = max(curMax,max1s)
            else:
                i+=1
        return max1s
    str = 'y'
    while(str == "y"):
        arr = list(map(int,input("Enter the array : ").strip().split()))
        print(findMaxConsecutiveOnes(arr))
        str = input("Enter 'y' for more :")
    print("Program run successfully ")