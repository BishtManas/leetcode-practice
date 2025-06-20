class Solution:
    def reverseWords(self, s):
        word = s.split()
        rev_word = [letter[::-1] for letter in word]
        return (' '.join(rev_word))
    
info = Solution()
print(info.reverseWords("Let's take LeetCode contest"))
# output :- s'teL ekat edoCteeL tsetnoc