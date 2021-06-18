# 690. Employee Importance
def getImportance( employees, id):
    empMap, queue, result = {},[],0
    for emp in employees:
        empMap[emp.id] = emp
    queue.append(empMap[id])
    while len(queue) > 0 :
        node = queue.pop(0)
        result += node.importance 
        for emp in node.subordinate:
            queue.append(empMap[emp])
    return result 
    