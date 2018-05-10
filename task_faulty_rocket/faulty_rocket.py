import time


# STRING: 0.02946019172668457
# RJESENJE: 11101100111110011111011101011101
# 11101100111110011111011101011101

# RJESENJE: 11101100111110011111011101011101

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
            variables[variable_name] = int(variable_value, 2)
    return expression, variables


def is_one(value):
    return int(value) == 1


def perform_operation(first_value, second_value, operator):
    if operator == "&":
        return first_value & second_value
    elif operator == "|":
        return first_value | second_value
    else:
        return first_value ^ second_value


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
    result = bin(result)[2:]
    if len(result) < 32:
        diff = 32 - len(result)
        for i in range(diff):
            result = "0" + result
    return result


if __name__ == '__main__':
    start = time.time()
    string = "j^r|v|p|e&k&z&w|u^v&r&l|j&q&e|s^f&f|s^r^o^c^y&b&g&e|k&j|g^w|u&u^m^a&b&k&r|l|n&c&s|x^t^m^e|v&r|q^u^t^u^z&c\na 10100010001000110010111101000000\nc 00110101001010100111010001011111\nb 00100011001001100010111011111011\ne 10100010001101000111011011100110\ng 10010001010011111101011101100001\nf 00111111000111000110110111011101\nk 11101100011011111001010010001011\nj 00010001110010111001100101100000\nm 00110010101100001010000000010100\nl 11110100000010001011100101100010\no 01110011001000101101111010000001\nn 11001100010110101011101010010101\nq 00111010101001101001101101000101\np 10101011011011010110110111110011\ns 10001011101100011111011110000100\nr 11101000001000110011111110110001\nu 11001110001100001110010000000011\nt 01000111111000000111111010010010\nw 10010100000101001000110101010101\nv 01111001001011010101101011001101\ny 10111010111011110010111000001110\nx 01000011011011001110010101111010\nz 00011100010111100000101001000001"
    print(get_solution(string))
    end = time.time()
    print(end - start)

