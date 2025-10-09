from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_perfect = set(wordlist)
        words_cap = {}
        words_vowel = {}
        
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)
        
        for word in wordlist:
            low = word.lower()
            if low not in words_cap:
                words_cap[low] = word
            v = devowel(low)
            if v not in words_vowel:
                words_vowel[v] = word
        
        ans = []
        for q in queries:
            if q in words_perfect:
                ans.append(q)
            else:
                low = q.lower()
                if low in words_cap:
                    ans.append(words_cap[low])
                else:
                    v = devowel(low)
                    if v in words_vowel:
                        ans.append(words_vowel[v])
                    else:
                        ans.append("")
        return ans


# ----------------- Local Testing -----------------
if __name__ == "__main__":
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    
    sol = Solution()
    result = sol.spellchecker(wordlist, queries)
    print("Output:", result)
