class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)# using set method.
info = Solution()
print(info.intersection([1,2,2,1],[2,2]))