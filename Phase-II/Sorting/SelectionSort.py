arr = [2,4,1,1,0,9,8,7,6]
n = len(arr)
def SelectionSort(nums,n):
    if n == 1 : return
    max_ele_index = n-1
    for i in range(n-1):
        if nums[i] > nums[max_ele_index]:
            max_ele_index = i
    if max_ele_index != n-1:
        nums[max_ele_index],nums[n-1] = nums[n-1],nums[max_ele_index]
    SelectionSort(nums,n-1) 
    return nums
print(SelectionSort(arr,n))