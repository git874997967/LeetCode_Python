#1134. Armstrong Number
from typing import OrderedDict


def isArmstrong(n):
    numSum , bit = 0, len(str(n))
    ori = n
    while n > 0 :
        numSum += (n % 10) ** bit 
        n = n // 10
    return  numSum == ori 

def find():
    for i in range(10000000):
        if isArmstrong(i):
            print(i)
find()