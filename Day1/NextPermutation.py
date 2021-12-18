# Problem Link: https://leetcode.com/problems/next-permutation/


def nextPermutation(arr):
    trans = -1
    transIndx = -1
    for i in range(len(arr) - 1, 0, -1):

        if arr[i] > arr[i - 1]:
            trans = arr[i - 1]
            transIndx = i - 1
            break

    if transIndx == -1:
        arr.reverse()
        return

    nxtGr = 10000
    nxtIn = -1

    # finding nxt greater element in right side of array
    for i in range(transIndx + 1, len(arr)):

        if arr[i] > trans and arr[i] <= nxtGr:
            nxtGr = arr[i]
            nxtIn = i

    # swap with nxt greater element
    arr[transIndx], arr[nxtIn] = arr[nxtIn], arr[transIndx]

    lastIndx = len(arr) - 1
    while (transIndx + 1 < lastIndx):
        arr[transIndx + 1], arr[lastIndx] = arr[lastIndx], arr[transIndx + 1]
        transIndx += 1
        lastIndx -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 6, 5, 4]
    nextPermutation(arr)
    print(arr)
