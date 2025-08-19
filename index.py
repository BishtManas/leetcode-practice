from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())

if __name__ == "__main__":
    # Sample input
    sample = ["eat","tea","tan","ate","nat","bat"]
    result = group_anagrams(sample)
    print("Input:", sample)
    print("Grouped anagrams:", result)

    # Quick assertions / tests
    def as_sets(lol):  # normalize order for comparison
        return set(tuple(sorted(group)) for group in lol)

    expected = [["bat"], ["nat","tan"], ["ate","eat","tea"]]
    assert as_sets(result) == as_sets(expected)
    print("All tests passed ✅")