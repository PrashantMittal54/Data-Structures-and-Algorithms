# Implement an algorithm to determine if a string has all unique characters or not.


def is_unique(input_str):
    otp = {}
    input_str = input_str.replace(" ", "").lower()
    for s in input_str:
        if s in otp:
            return False
        else:
            otp[s] = 1
    else:
        return True


unique_str = "AbCDefG"
non_unique_str = "non Unique STR"

print(is_unique(unique_str))
print(is_unique(non_unique_str))
