def romanToInt(s: str) -> int:
    result = 0
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    i = len(s) - 1

    while i >= 0:
        curr_roman = s[i] 
        if i < len(s) - 1 and (roman_dict[curr_roman] < roman_dict[s[i+1]]):
            result -= roman_dict[curr_roman]
        else:
            result += roman_dict[curr_roman]
        i-=1
    return result

print(romanToInt("IV"))