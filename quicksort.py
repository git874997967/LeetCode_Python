
# 又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。
# 它是处理大数据最快的排序算法之一，虽然 Worst Case 的时间复杂度达到了 O(n²)，但是在大多数情况下都比平均时间复杂度为 O(n log n) 的排序算法表现要更好，
# 因为 O(n log n) 记号中隐含的常数因子很小，而且快速排序的内循环比大多数排序算法都要短小，这意味着它无论是在理论上还是在实际中都要更快，
# 比复杂度稳定等于 O(n log n) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
# 它的主要缺点是非常脆弱，在实现时要非常小心才能避免低劣的性能。
import time
import numpy as np
# 这种写法平均空间复杂度 nlogn
def quickSort(num):
    # base case 
    if len(num) <= 1:
        return num
    pivot = num[0] # 基准值
    left = [num[i] for i in range(1,len(num)) if num[i]< pivot]
    right = [num[i] for i in range(1,len(num)) if num[i] >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)
# 这种写法平均空间复杂度 logn
def quickSort2(nums, left, right):
    # 分区操作 
    def partition(nums,left,right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] > right:
                right -= 1
            # 比基准小的切换到前面    
            nums[left] = nums[right] 
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right]  = nums[left]
        nums[left] = pivot
        return left
    if left < right:
        pivotIndex = partition(nums,left,right)
        quickSort2(nums,left,pivotIndex -1)
        quickSort2(nums,pivotIndex + 1, right)
def mergeSort(num):
    def sort(left,right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]
    # base case
    if len(num) <= 1:
        return num
    mid = len(num)//2
    left = mergeSort(num[:mid])
    right = mergeSort(num[mid:])
    return sort(left,right)

num = np.random.randint(1,5000000,1000000)
quick_start = time.time()
result = quickSort(num)
quick_stop =  time.time() - quick_start 
print(f'it last {quick_stop} s for quickSort ')
merge_start = time.time()
result2 = mergeSort(num)
merge_end = time.time() - merge_start
print(f'it last {merge_end} s for mergeSort')



 

