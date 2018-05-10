from sortedcontainers import SortedList


def get_solution(string):
    lines = string.split("\n")
    heights = [float(x) for x in lines[1:]]
    taller_count = [0 for x in heights]
    people_sorted = SortedList()

    sum = 0
    for i in range(len(heights)):
        people_sorted.add(heights[i])
        taller_count[i] = i - people_sorted.index(heights[i])
        sum += taller_count[i]

    return str(sum)


if __name__ == '__main__':
    print(get_solution("5\n10\n6\n15\n20\n30\n5\n7"))