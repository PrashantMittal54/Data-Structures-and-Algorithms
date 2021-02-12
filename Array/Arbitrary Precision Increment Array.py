def plus_one(A):
    A[-1] += 1
    carry = 0
    for x in range(1,len(A)+1):
        if (A[-x] + carry) == 10:
            carry = 1
            A[-x] = 0
        else:
            A[-x] += carry
            break
    if A[0] == 0:
        A[0] = 1
        A.append(0)
    return A


print(plus_one([2,9,9]))
print(plus_one([9,9,9]))
