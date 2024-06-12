arr = [2,4,1,1,0,9,8,7,6]
n = len(arr)
def Bubble_sort(nums,n):
    if n == 1:
        return
    for i in range(n-1):
        if nums[i] > nums[i + 1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
    Bubble_sort(nums,n-1)
    return nums
print(Bubble_sort(arr,n))
