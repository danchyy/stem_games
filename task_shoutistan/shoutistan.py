from time import time

def calculate_leading_zeros(number, target_zeros, is_exact=False):
    five_squared = 5
    amount_of_zeros = 0
    while five_squared < number:
        amount_of_zeros += (number // five_squared)
        five_squared = five_squared * 5
    if is_exact:
        return amount_of_zeros == target_zeros
    return amount_of_zeros >= target_zeros

def get_solution(string):
    number_of_zeros = int(string)

    maximal = 5 * number_of_zeros
    minimal = 0
    while minimal < maximal:
        mid = (maximal + minimal) >> 1

        if calculate_leading_zeros(mid, number_of_zeros):
            maximal = mid
        else:
            minimal = mid + 1

    if calculate_leading_zeros(minimal, number_of_zeros, is_exact=True):
        result = str(minimal)
        temp = minimal + 1
        while calculate_leading_zeros(temp, number_of_zeros, is_exact=True):
            result = result + " " + str(temp)
            temp += 1
        return result
    else:
        return "-1"


if __name__ == '__main__':
    start = time()
    print(get_solution(23))
    end = time()
    print(end - start)