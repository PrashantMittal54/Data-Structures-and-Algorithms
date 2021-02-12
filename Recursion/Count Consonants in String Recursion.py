# count consonants of a string using recursive approach


def recursive_count_consonants(input_str):
    vowels = 'aeiou'
    if not input_str:
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


input_str = "LuCiDPrograMMiNG"
input_str1 = "abc de"

print(recursive_count_consonants(input_str))
