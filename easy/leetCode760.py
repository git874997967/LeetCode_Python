# 760. Find Anagram Mappings
def anagramMappings(nums1, nums2):
    numMap = {}
    
    for k,v in enumerate(nums2):
        numMap[v] = numMap.get(v,k)

    for i in range(0,len(nums1)):
        nums1[i] = numMap[nums1[i]]
    return nums1


print(anagramMappings([12,28,46,32,50],[50,12,32,46,28]))

print(anagramMappings([84,46],[84,46]))

print(anagramMappings([84,46],[84,46,84]))

