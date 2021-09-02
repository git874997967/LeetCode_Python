#1491. Average Salary Excluding the Minimum and Maximum Salary
def average( salary):
    return sum(salary) - max(salary) - min(salary) // (len(salary) - 2)