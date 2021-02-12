# Develop an algorithm to return the first occurring uppercase letter


def find_uppercase_recursive(input_str, idx=0):
    if idx == len(input_str)-1:
        return "No upper case letter"
    if input_str[idx].isupper():
        return input_str[idx]
    else:
        return find_uppercase_recursive(input_str, idx+1)


input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"
print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))