
def parse_input(string):
    """
    a & b & ....
    a 1001000....
    :param string:
    :return:
    """
    splitted_lines = string.split("\n")
    first = True
    expression = ""
    variables = {}
    for line in splitted_lines:
        if first:
            expression = line.strip()
            first = False
        else:
            splitted_variable_line = line.split(" ")
            variable_name = splitted_variable_line[0]
            variable_value = splitted_variable_line[1]
            variables[variable_name] = variable_value
    return expression, variables


def is_one(value):
    return int(value) == 1


def perform_operation(first_value, second_value, operator):
    result_string = ""
    for i in range(len(first_value)):
        first_char, second_char = first_value[i], second_value[i]
        if operator == "&":
            if is_one(first_char) and is_one(second_char):
                result_string += "1"
            else:
                result_string += "0"
        elif operator == "|":
            if is_one(first_char) or is_one(second_char):
                result_string += "1"
            else:
                result_string += "0"
        else:
            if is_one(first_char) and not is_one(second_char):
                result_string += "1"
            elif not is_one(first_char) and is_one(second_char):
                result_string += "1"
            else:
                result_string += "0"
    return result_string


def get_solution(string):
    expression, variables = parse_input(string)
    operators = ['&', '|', '^']
    result = None
    curr_operator = ""
    for char in expression:
        if char in variables:
            value = variables[char]
            if result is None:
                result = value
                first_value = value
            elif curr_operator != "":
                result = perform_operation(result, value, curr_operator)
        else:
            curr_operator = char
    return result


if __name__ == '__main__':
    string = "a&b|c^d\na 11000000000000000000000000000010\nb 01000000000000000000000000000001\nc 00010000000000000000000000000011\nd 00011000000000000000000000000010"
    print("\nr: " + get_solution(string))

