#759. Employee Free Time
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
     

class Solution(object):
    def employeeFreeTime( schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        result,arr = [],[]
        for intervals in schedule:
            for interval in intervals:
                arr.append(interval)
        arr.sort(key = lambda x:x[0])
        work = arr[0]
        for i in range(1,len(arr)):
            if work[1] < arr[i][0]: ## we do have the gap
                result.append([work[1],arr[i][0]])
                work = arr[i]
            elif work[1] <= arr[i][1]: ## update the work period 
                work[1] = arr[i][1]
        return result


schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
schedule2 =  [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
print(Solution.employeeFreeTime(schedule2))