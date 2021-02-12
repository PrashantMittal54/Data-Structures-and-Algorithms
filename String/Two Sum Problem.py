# Time Complexity: O(n)
# Space Complexity: O(n)
# Solution 1


def two_sum_hash_table(A, target):
    tbl = {}
    for x in A:
        if x in tbl:
            print((tbl[x], x))
            return True
        else:
            tbl[target-x] = x
    return False

# Solution 2
# Time Complexity: O(n)
# Space Complexity: O(1)


def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print((A[i], A[j]))
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum_hash_table(A, target))
print(two_sum(A, target))

