

def get_solution(string):
    stack = []

    opening = ["[", "{", "("]
    closing = ["]", "}", ")"]
    for char in string:
        if char in closing:
            if len(stack) == 0:
                return "F"
            if opening.index(stack[-1]) == closing.index(char):
                stack.pop(-1)
            else:
                return "F"
        else:
            stack.append(char)

    if len(stack) == 0:
        return "T"
    else:
        return "F"
