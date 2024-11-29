def findMedianSortedArrays(nums1, nums2):
    nums3  = sorted(nums1 + nums2)
    total_len = len(nums3)
    
    if total_len % 2 == 0:
        print(nums3[total_len // 2-1 ], nums3[total_len // 2] )
        return (nums3[total_len//2] + nums3[total_len//2 - 1]) / 2
    
    else:
        return nums3[total_len//2 + 1]
    

print(5/2 )