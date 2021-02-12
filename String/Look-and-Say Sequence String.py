# Look-and-Say Sequence
# To generate a member of the sequence from the previous member, read off the digits of the previous member
# and record the count of the number of digits in groups of the same digit.
# 
# For example, 1 is read off as one 1 which implies that the count of 1 is one. As 1 is read off as “one 1”,
# the next sequence will be written as 11 where 1 replaces one. Now 11 is read off as “two 1s” as the count
# of “1” is two in this term. Hence, the next term in the sequence becomes 21.


def next_number(s):
    idx = 0
    output = []
    while idx < len(s):
        count = 1
        while idx+1 < len(s) and s[idx] == s[idx+1]:
            count += 1
            idx += 1
        output.append(str(count))
        output.append(s[idx])
        idx += 1
    return ''.join(output)


s = "1"
print(s)
n = 8
for i in range(n-1):
    s = next_number(s)
    print(s)
