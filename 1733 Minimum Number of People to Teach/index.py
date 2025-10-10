from collections import defaultdict

class Solution:
    def minimumTeachings(self, n, languages, friendships):
        m = len(languages)
        
        # Convert each user's language list into a set for fast lookup
        lang_sets = [set(l) for l in languages]
        
        # Step 1: Find all friendship pairs that can't communicate
        to_fix = set()
        for u, v in friendships:
            u -= 1  # Make zero-based index
            v -= 1
            if lang_sets[u].intersection(lang_sets[v]):
                continue  # They can already talk
            to_fix.add((u, v))

        # Step 2: For each language, find how many users we need to teach it to fix all broken pairs
        min_teach = float('inf')
        
        for lang in range(1, n + 1):
            teach_set = set()
            for u, v in to_fix:
                if lang not in lang_sets[u]:
                    teach_set.add(u)
                if lang not in lang_sets[v]:
                    teach_set.add(v)
            min_teach = min(min_teach, len(teach_set))
        
        return min_teach
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    n = 2
    languages = [[1],[2],[1,2]]
    friendships = [[1,2],[1,3],[2,3]]
    print(sol.minimumTeachings(n, languages, friendships))  # Output: 1

    # Test Case 2
    n = 3
    languages = [[2],[1,3],[1,2],[3]]
    friendships = [[1,4],[1,2],[3,4],[2,3]]
    print(sol.minimumTeachings(n, languages, friendships))  # Output: 2
