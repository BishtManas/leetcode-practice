from collections import Counter

def intersect(nums1, nums2):
    count1 = Counter(nums1)  # count elements in nums1
    count2 = Counter(nums2)  # count elements in nums2
    result = []

    for num in count1:
        if num in count2:
            # add the common number min times
            times = min(count1[num], count2[num])
            result.extend([num] * times)
    
    return result
print(intersect([4,9,5], [9,4,9,8,4]))
