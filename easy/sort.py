#quick sort
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
def quickSort2(arr, low, high):
    def partition(arr, low, high):
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot
    
        for j in range(low, high):
    
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
    
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
    
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort2(arr, low, pi-1)
        quickSort2(arr, pi+1, high)
# Merge Sort
# 归并排序须知：
# 作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

# 自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第2种方法）
# 自下而上的迭代
# 和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，
# 因为始终都是O(n log n）的时间复杂度。代价是需要额外的内存空间。
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

num1 = num2 = num3 = np.random.randint(1,5000000,1000000)
merge_start = time.time()
mergeSort(num3)
merge_end = time.time() - merge_start
print(f'it last {merge_end} s for mergeSort')
quick_start = time.time()
quickSort(num1)
quick_stop =  time.time() - quick_start 
print(f'it last {quick_stop} s for quickSort ')
quick2_start = time.time()
quickSort2(num1,0,len(num1)-1)
quick2_stop = time.time() - quick2_start
print(f'it last {quick2_stop} s for quickSort2 ')




 

