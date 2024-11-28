def numberOfEmployeesWhoMetTarget(hours,target):
    return sum(1 if hour >= target else 0 for hour in hours)