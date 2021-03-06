# 349. Intersection of Two Arrays
def intersection( nums1, nums2):
    result = []
    dict1, dict2,dict3= {},{},{}
    for num in nums1:
        if num  not in dict1.keys():
            dict1[num] = 1
        else:
            dict1[num] += 1
    for num in nums2:
        if num not in dict2.keys():
            dict2[num] = 1
        else:
            dict2[num] += 1
    if len(dict1) <= len(dict2):
        for key in dict1.keys():
            if key in dict2.keys():
                dict3[key] = min(dict1[key],dict2[key])  
    else:
        for key in dict2.keys():
            if key in dict1.keys():
                dict3[key] = min(dict1[key],dict2[key])
    for key in dict3.keys():
        value = dict3[key]
        while(value):
            result.append(key)
            value -= 1
    print(result)
    return result

num1 = [3,1,2]
num2 = [1,1]

# two pointers 
