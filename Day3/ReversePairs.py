cnt = 0

def reversePairs(nums):
            global cnt
            def mergeSort(arr):
                global cnt
                if len(arr) > 1:

                    mid = len(arr) // 2

                    L = arr[:mid]
                    R = arr[mid:]

                    mergeSort(L)
                    mergeSort(R)

                    i = j = k = 0

                    rp = 0
             # check for every pair in both arrays L and Right
                    for lp in range(len(L)):

                        while(rp < len(R) and ((2*R[rp]) < L[lp])):
                            print((L[lp],R[rp]))
                            rp+=1
                        cnt+=rp
                    while i < len(L) and j < len(R):
                        if L[i] <= R[j]:
                            arr[k] = L[i]
                            i += 1
                        else:
                            arr[k] = R[j]
                            j += 1
                        k += 1
                    while i < len(L):
                        arr[k] = L[i]
                        i += 1
                        k += 1

                    while j < len(R):
                        arr[k] = R[j]
                        j += 1
                        k += 1
            mergeSort(nums)



nums = [2,4,3,5,1]
reversePairs(nums)
print("Number of Pairs : ",cnt)




