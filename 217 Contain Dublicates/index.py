class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen :
                return True
            seen.add(num)
        return False
info = Solution()
print(info.containsDuplicate([1,2,3,3,4,2,5]))# True, because duplicate is present in this case.
print(info.containsDuplicate([1,2,3,4]))# False, because duplicate is not present.