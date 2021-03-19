import math
import unittest

class Solution:
    def get_free_time(self,calendar1,calendar2,duration, time):
        if time[0] >= time[1]:
            return []
        start, end = 0, 1
        free_calendar1 = self.get_free_calendar(calendar1,time[0],time[1])
        free_calendar2 = self.get_free_calendar(calendar2,time[0],time[1])
        free_time = self.merge_calendars(free_calendar1,free_calendar2)
        print(free_time)
        result =[]
        last_start = 0
        free_people = 0
        for time,type in free_time:
            if type == start:
                free_people+=1
                last_start = time
            else:
                if free_people ==2:
                    if time - last_start >=duration:
                        result.append((last_start,time))
                free_people -=1

        return result

    def get_free_calendar(self,calendar,start,end):
        temp_start= start
        result = []
        if not calendar:
            return [(start,end)]
        for s, e in calendar:
            if e < start:
                continue
            if s > end:
                continue
            if s- temp_start>=0:
                free_start,free_end = temp_start,s
                if free_end>free_start:
                    result.append((free_start,free_end))
                temp_start = e
            else:
                temp_start = e
        if temp_start<end:
            result.append((temp_start,end))
        return result

    def merge_calendars(self,calendar1, calendar2):
        result = []
        start,end = 0,1
        for s,e in calendar1:
            result.append((s,start))
            result.append((e,end))
        for s, e in calendar2:
            result.append((s, start))
            result.append((e, end))
        result.sort()
        return result

# For unit test only
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

    def test_get_free_calendar1(self):
        calendar = [(20, 100), (200, 230), (250, 330)]
        time = (0, 500)
        s = Solution()
        result = s.get_free_calendar(calendar,time[0],time[1])
        correct_answer = [(0, 20), (100, 200), (230, 250), (330, 500)]
        self.assertEqual(result,correct_answer)

    def test_get_free_calendar2(self):
        calendar = [(10, 20), (200, 230), (250, 330)]
        time = (30, 300)
        s = Solution()
        result = s.get_free_calendar(calendar,time[0],time[1])
        correct_answer = [ (30, 200), (230, 250)]
        self.assertEqual(result,correct_answer)

    def test_get_merge_calendars(self):
        calendar1 = [(20,100),(200,230),(250,330)]
        calendar2 = [(30,100),(100,130),(250,330)]
        s = Solution()
        time = (0,500)
        calendar1 = s.get_free_calendar(calendar1,time[0],time[1])
        calendar2 = s.get_free_calendar(calendar2,time[0],time[1])
        result = s.merge_calendars(calendar1,calendar2)
        correct_answer = [(0, 0), (0, 0), (20, 1), (30, 1), (100, 0), (130, 0), (200, 1), (230, 0), (250, 1), (250, 1), (330, 0), (330, 0), (500, 1), (500, 1)]
        self.assertEqual(result,correct_answer)
    def test_get_free_time1(self):
        calendar1 = []
        calendar2 = [(20,200)]
        duration = 10
        time = (0,500)
        s = Solution()
        result = s.get_free_time(calendar1,calendar2,duration,time)
        correct_answer = [(0,500)]
        self.assertEqual(result,correct_answer)


if __name__ == '__main__':
    unittest.main()