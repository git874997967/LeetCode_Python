# def twoOutOfThree( nums1, nums2, nums3):
#     map1,map2,map3 = {},{},{}
#     result,key_set = [], set()
#     for num in nums1:
#         map1[num] = map1.get(num,0) + 1
#         key_set.add(num)
#     for num in nums2:
#         map2[num] = map2.get(num,0) + 1
#         key_set.add(num)
#     for num in nums3:
#         map3[num] = map3.get(num,0) + 1 
#         key_set.add(num)
        
#     for key in key_set:
#         time = 0
#         if key in map1.keys():
#             time += 1
#         if key in map2.keys():
#             time += 1
#         if key in map3.keys():
#             time += 1
#         if time >= 2:
#             result.append(key)
#     return result
def twoOutOfThree(nums1, nums2, nums3):
    result_list = []
    num_set = set()
    for num in nums1:
         
        num_set.add(num)
    for num in nums2:
        num_set.add(num)
       
    for num in nums3:
        if num in num_set:
            result_list.append(num)
       
    return result_list



nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
print(twoOutOfThree(nums1, nums2, nums3))
nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
print(twoOutOfThree(nums1, nums2, nums3))
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(twoOutOfThree(nums1, nums2, nums3))