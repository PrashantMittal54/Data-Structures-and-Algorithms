# Convert the string you are given to an integer.


def str_to_int(input_str):
    neg = False
    if input_str[0] == '-':
        neg = True
        input_str = input_str[1:]
    num = 0
    power = len(input_str) - 1
    for s in input_str:
        num += (ord(s)-ord('0'))*(10**power)
        power -= 1
    if neg:
        return num*-1
    else:
        return num


s1 = "123"
print(str_to_int(s1))

s2 = "-123"
print(str_to_int(s2))
