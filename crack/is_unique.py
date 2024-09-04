def is_unique(s):
    se = set()
    for letter in s:
        if letter in se:
            return False
        else:
            se.add(letter)
    return True

s = "aqwrtyui"
print(is_unique(s))
