# calculate the length of a string using recursive approach


def recursive_str_len(input_str):
    if not input_str:
        return 0
    else:
        return 1 + recursive_str_len(input_str[1:])


input_str1 = "LucidProgramming"

print(recursive_str_len(input_str1))
