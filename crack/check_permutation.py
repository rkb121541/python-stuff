from collections import defaultdict

def check_permutation(s1, s2):
    if len(s1) != len(s2): return False
    hm_s1, hm_s2 = defaultdict(), defaultdict()
    for letter in s1:
        hm_s1[letter] = hm_s1.get(letter, 0) + 1
        hm_s2[letter] = hm_s2.get(letter, 0) + 1
    if hm_s1.items() == hm_s2.items(): return True
    else: return False

s1 = "abbaa"
s2 = "bbaa"
print(check_permutation(s1, s2))
