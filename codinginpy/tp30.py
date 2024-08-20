if __name__ == "__main__":
    roman_numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    list_numerals = list(roman_numerals.keys())
    num = 1994
    result = ""
    i = -1
    while True:
        if num <= 0: break
        elif num - roman_numerals[list_numerals[i]] < 0: i -= 1
        else:
            num -= roman_numerals[list_numerals[i]]
            result += list_numerals[i]
    print(result) if result != "" else print(-1)
