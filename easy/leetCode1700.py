#1700. Number of Students Unable to Eat Lunch
from typing import Deque


from collections import deque 
def countStudents(students, sandwiches):
        dStudent, dSandwiches = deque(students),deque(sandwiches)
        size = len(dSandwiches)
        while dStudent  :
            dSnap = [i for i in students]
            if dStudent[0] == dSandwiches[0]:
                sandwish = dSandwiches.popleft()
                dStudent.popleft()
                size -= 1
            else:
                 dStudent.append(dStudent.popleft())
                 if dStudent == dSnap:
                     return len(dStudent)
            
        return len(dStudent)

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
countStudents(students=students,sandwiches= sandwiches)