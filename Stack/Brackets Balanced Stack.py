def check_balanced(left, right):
    if left == '{' and right == '}':
        return True
    elif left == '[' and right == ']':
        return True
    elif left == '(' and right == ')':
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    main_stack = []
    for x in paren_string:
        if x in '{[(':
            main_stack.append(x)
        elif x in ']})':
            # main_stack.append(x)
            if len(main_stack) != 0:
                left = main_stack.pop()
                status = check_balanced(left, x)
                if not status:
                    return False
            else:
                return False
    if len(main_stack) == 0:
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))
