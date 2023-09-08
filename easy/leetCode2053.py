# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
def kthDistinct(arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        if k > len(arr):
            return ""
        count_map = {}
        count = k
        for item in arr:
            count_map[item] = count_map.get(item,0) + 1
        print(count_map)
        for i in range(len(arr)):
            if count_map[arr[i]] == 1:
                count -= 1
                if count == 0:
                    return arr[i]
        return ""
    
arr = ['d','b','c','b','c','a']
k = 2
print(kthDistinct(arr, k))
arr1 = ['aaa','aa','a']
k1 = 1
print(kthDistinct(arr1, k1))
arr1 = ['a','b','a','c']
k1 = 2
print(kthDistinct(arr1, k1))

arr1 = ['dtby']
k1 = 1
print(kthDistinct(arr1, k1))