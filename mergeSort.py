# Merge Sort
# 归并排序须知：
# 作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

# 自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第2种方法）
# 自下而上的迭代
# 和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，
# 因为始终都是O(n log n）的时间复杂度。代价是需要额外的内存空间。
import time
import numpy as np
def mergeSort(num):
    def sort(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # handle the rest num 
        return result + left[i:] + right[j:] 
    # base case  
    if len(num) <= 1:
        return num
    mid = len(num)//2
    left = mergeSort(num[:mid])
    right = mergeSort(num[mid:])
    return sort(left,right)
def quickSort(num):
    # base case 
    if len(num) <= 1:
        return num
    pivot = num[0] # 基准值
    left = [num[i] for i in range(1,len(num)) if num[i]< pivot]
    right = [num[i] for i in range(1,len(num)) if num[i] >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)


num = np.random.randint(1,5000000,1000000)
since = time.time()
result = mergeSort(num)
dur = time.time() - since
print(f'it last {dur} s for mergeSort ')

quick_start = time.time()
result = quickSort(num)
quick_stop =  time.time() - quick_start 
print(f'it last {quick_stop} s for quickSort ')