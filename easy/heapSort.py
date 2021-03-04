# 堆排序须知：
# 堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：

# 大根堆：每个节点的值都大于或等于其子节点的值，用于升序排列；
# 小根堆：每个节点的值都小于或等于其子节点的值，用于降序排列。
import numpy as np
import time 
def heapSort(num):
    # 调整堆
    def adjustHeap(nums, i, size):
        # 非叶子节点左右孩子   必有两个孩子 因为满 
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        # 在当前三者中找到最大索引 
        largest = i
        if lchild < size and nums[lchild] > nums[largest]:
            largest = lchild
        if rchild < size and nums[rchild] > nums[largest]:
            largest = rchild
        # 如果最大元素的索引不是当前节点 把大的结点换到上面  继续调整堆
        if largest != i:
            # 高级用法交换值 
            nums[largest] , num[i] = nums[i] ,nums[largest] 
            adjustHeap(nums,largest,size)
    # 建立堆
    def buildHeap(nums,size):
        # 从倒数第一个结点到中间结点 逆序遍历
        for i in range(len(nums)//2)[::-1]: 
            adjustHeap(nums,i,size)
    size = len(num)
    buildHeap(num,size)
    for i in range(len(num))[::-1]:
        # 每次根节点都是最大的数字放在最后面 
        num[0],num[i] = num[i], num[0]
        # 交换后有重新调整堆 只需调整根节点  数组size不包括已经调整好的数组
        adjustHeap(num, 0 , i)
    return num
num = np.random.randint(1,5000000,1000000)
since = time.time()
result = heapSort(num)
dur = time.time() - since
print(f'it last {dur} s for heapSort ')