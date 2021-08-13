import queue
import collections
import heapq
from operator import itemgetter
def listExercise(arr):
    arr.append(11)
    arr.remove(3)
    del arr[3]
    arr = sorted(arr,reverse= False)
    arr.pop(-2)
    arr.pop(0)
    arr.append(11)
    print(arr.count(11) )
    for i in range(0,len(arr)):
        print(arr[i])
   
# def tupleExercise(args):
#  pass 
def dictExercise(map):
    print(map.get("Boss","未知元素"))
    map.setdefault("未知key","abcdefg")
    # for key in map.keys():
    #     print(key, map.get(key,"未知元素"))
    # myMap = {}
    # for i in range(65,74):
    #     myMap[chr(i)] = i
     
    # for key, item in myMap.items():
    #     print(key,item)
    # newMap = sorted(myMap.items(), key = lambda item:item[1], reverse= False)
    # for key, item in newMap :
    #     print(key,item)
#  count the freq for each number
    testArr = [1,2,45,7,8,2,9,45,1,0,8,8,7,7,7]
    countMap = {}
    curMax = float('-inf')
    for i in testArr:
        count = countMap.get(i,0) + 1
        curMax = max(count,curMax)
        countMap[i] = count
    print("the most freq num is "+ str(curMax))
    for key, val in countMap.items():
        print(key,val)



def stackExercise(stack):
    for i in range(10,20,2):
        stack.append(i)
    print(stack.pop())
    print(stack[-1]) # peek
    for i in stack:
        print(i,sep= '\t',end= '\t')

def  FIFO(q):
    size = len(q)

    while not q.empty():
        print(q.get())

# class priorityQueue(priority,name):
#     def __init__(self, priority, name):
#       self.priority = priority
#       self.name = name
#     def __cmp__(self,other):
#         return cmp(self.priority, other.priority)
 
def heapExercise(heap):
     heapq.heappush(heap,2)
     heapq._heapify_max(heap)
     
     for num in heap:
         print(num)
def dequeExercise(deque):
    doubleEnd = collections.deque(deque)
    doubleEnd.appendleft(100)
    doubleEnd.popleft()
 
# q = queue.PriorityQueue()
# q.put(priorityQueue(100,"not urgent"))
# q.put(priorityQueue(4,'important'))
# q.put(priorityQueue(1,"urgent task"))
# while not q.empty():
#     cur_name = q.get()
#     print("process task " + cur_name)
#arr = [1,2,3,4,5,6,7,8,9,0]
# listExercise(arr)
dictExercise({"Name":"ABC","AGE":"7","Class":"First"})
# stackExercise(arr)
# FIFO(q)
# priorityQueue(q)

# heapExercise([0,9,8,7,5,4,3,1,2])
# dequeExercise(arr)
 