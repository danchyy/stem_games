import time


# STRING: 0.02946019172668457
# RJESENJE: 11101100111110011111011101011101

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
    return result[2:]


if __name__ == '__main__':
    start = time.time()
    string = "v|i^j|h&r&r&w&f|s^y^h&o&n|x^g&s|s^t&t|d^g^q|g|i|p&f&x^k|i^d&n&r|k|v&y^z|r|d|v&x|r&q^u|f^p&a^e^g&n|p&u&t|t^z&v|j^i^d^e&e|p&j|e^a|u&q&u|g&o^o|o^a&p|y&x|t&m&x^y^r&y^a|w&v^b^a|v^b|j|f&n^n&r^d^m^c&g&h&y|v&n&x^f^k|y|c&g&f|t&a^d&n|s^b^h|f&s&l|d|c^s&s|x&s|v&w^k&d&k^o&e|v^n&n&f^s&m&o&z|e^u|j&c|v|e^j^x&i&w&r&c^y^a|m|k|y|w^d|o|f^k&w^t^j&j^f&o|n^n^u^m&s&t|f&t|h&c&a^v^y&f|s^h|d&p&a&f&f&n^s&t^n&b^v^x|o&d&t&o|k^i&l^r&r^y|y|q^x^k|w|p&e^w^d^p^s^z|d&e&e^u|l&s&h|i&h&p|y^l|k|f|w|b^y|a^y|d^h^e|k^r^z&j^t&h^c&n|h&k|n&p^o^q|b^j^f|v^n|f&m^j&c&y|y&e&o^r^k|u^m^b|i|s&k^e|h|b&x&f|l&x&t|c|w^m^p^c&y&n^n|y&a^b&o|n&r|c^u|t^q&r|k^x^m&o|r^c&c^c&o&w^u&g|j^v|t|e^c^g^v|o^y^q^c^s&f&y&h&j|m|c|k|f|z&b|m&b|l&a^w|h|b&c&n^h&p|m|i^h^f&l^c&r&l|i|b^p&t|n|w&g&p&b&t^f&l|t&x^r^f&m&v&i^z|g|k|p&r^s^x^o&l|n&j|f&v&w&l|q^f|z|g^u^s|u&o&o|c&d|i&t^y&h&r|g&p|q&r&u&o&o^k&a&g&k^u^o^w^m|r|s|t&u&w|b&x^e&h|o|k|n|n^e&o|j|r^j&x&w&g^x^w^z^f|l|v&n|e&h&c^g|c|w&i&a^z|v|u|p^y|f|s|i|v|i&m|v|h&i|c|s|j^n\na 00000011110110001101110001101000\nc 01000100101110110011010010100110\nb 00100010101110110011100101010000\ne 00101011100110011100100111110100\nd 00011000010110101111000100111111\ng 10011010110111010111101111110110\nf 00101011010011000010100011111101\ni 01000011010110110010110110100110\nh 00100010001011111010101001001101\nk 01110110000011010100110010100000\nj 10000110111101110110011000100000\nm 00001111011000011011011010011000\nl 00100001100000100011001001100001\no 01011100000111101011000111011100\nn 00011011000001100000100011100011\nq 11110011110100111001001101000010\np 00111100100011001001001010111101\ns 11110000101110101101010110011010\nr 10101111011111111101001010101110\nu 11110110101110101100011100000100\nt 10101010110010011100000001100101\nw 00010000111000001100000110000011\nv 10100111100111111111111001110110\ny 00100011100011111101001011111000\nx 10111100010000010101100111000101\nz 00110011000111011110011001000100"
    print(bin(get_solution(string))[2:])
    end = time.time()
    print(end - start)

