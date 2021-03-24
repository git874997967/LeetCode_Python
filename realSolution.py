import unittest
class Solution:
    def get_free_time(self,cal1,cal2,duration,time):
        free1,free2,result = [],[],[]
        def get_free(cal, time):
            if not cal:
                return[[time[0],time[1]]]
            busy, freeList = list(cal[0]), []
            # check if the busy time is the start time
            if cal[0][0] != time[0]:
                freeList.append([time[0],cal[0][0]])
            for i in range(len(cal)):
                if cal[i][0] > busy[1]:
                    freeList.append([cal[i-1][1],cal[i][0]])
                    busy = list(cal[i])
                else:
                    busy[1] = max(cal[i][1],busy[1])
            # check if the busy time is the end time
            if cal[-1][1] != time[1]:
                freeList.append([cal[-1][1],time[1]])
            return freeList
        free1,free2 = get_free(cal1,time), get_free(cal2,time)
        index1, index2 = 0,0
        while index1< len(free1) and index2 < len(free2):
            meetingStart = max(free1[index1][0],free2[index2][0])
            meetingEnd = min(free1[index1][1], free2[index2][1])
            if meetingEnd - meetingStart >= duration:
                result.append((meetingStart,meetingEnd))
            # move the pointer to the next slot 
            if free1[index1][1] <= free2[index2][1]:    
                index1 += 1
            else:  
                index2 += 1
        return result

class UnitTest(unittest.TestCase):
    def test_get_free_time1(self):
        calendar1 = [(20,100),(200,230),(250,330)]
        calendar2 = [(30,100),(100,130),(250,330)]
        duration = 10
        time = (0,500)
        s = Solution()
        result = s.get_free_time(calendar1,calendar2,duration,time)
        correct_answer = [(0, 20), (130, 200), (230, 250), (330, 500)]
        self.assertEqual(result,correct_answer)
    def test_get_free_time2(self):
        calendar1 = []
        calendar2 = [(20,200)]
        duration = 10
        time = (0,500)
        s = Solution()
        result = s.get_free_time(calendar1,calendar2,duration,time)
        correct_answer = [(0, 20), (200, 500)]
        self.assertEqual(result,correct_answer)
if __name__ == '__main__':
    unittest.main()
