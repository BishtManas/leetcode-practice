def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in map_s_t and map_s_t[char_s] != char_t:
            return False
        if char_t in map_t_s and map_t_s[char_t] != char_s:
            return False
        map_s_t[char_s] = char_t
        map_t_s[char_t] = char_s

    return True


# ✅ Testing
s = input("Enter first string: ")
t = input("Enter second string: ")

print("Isomorphic:", is_isomorphic(s, t))