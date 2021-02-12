# Given two numbers, find their product using recursion.


def recursive_multiply(x, y):
    if y > x:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    else:
        return x + recursive_multiply(x, y-1)


x = 500
y = 2000

print(x * y)
print(recursive_multiply(x, y))
