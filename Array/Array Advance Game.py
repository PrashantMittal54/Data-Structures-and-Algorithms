# Each number in the array represents the maximum you can advance in the array,
# find whether its possible to reach till the end of the array or not.


def array_advance(A):
    furthest_go = 0
    final_index = len(A) - 1
    i = 0
    while (i <= furthest_go) and (furthest_go < final_index):
        furthest_go = max(furthest_go, A[i] + i)
        i += 1
    if furthest_go >= final_index:
        return True
    else:
        return False


# False: Not possible to navigate to last index in A:
a = [3, 3, 1, 0, 0, 0, 1]
# True: Possible to navigate to last index in A:
b = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(a))
print(array_advance(b))
