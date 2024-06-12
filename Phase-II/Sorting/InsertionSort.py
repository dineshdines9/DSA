arr = [2,4,1,1,0,9,8,7,6]
n = len(arr)
def Insertion_sort(nums,n):
    if n == 1: return
    Insertion_sort(nums, n - 1)
    # nums = [1, 3, 4, 5, 6, 7, 8, 2]
    # nums = [1, 3, 3, 4, 5, 6, 7, 8]
    currValue = nums[n - 1]
    prevIndex = n - 2
    while prevIndex >= 0:
        if nums[prevIndex] > currValue:
            nums[prevIndex + 1] = nums[prevIndex]
        else:
            break 
        prevIndex -= 1 
    nums[prevIndex + 1] = currValue
    return nums
print(Insertion_sort(arr,n))