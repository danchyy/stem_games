

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def get_solution(string):
    lines = string.split('\n')
    n = int(lines[0])
    m = int(lines[1])
    weights = lines[2].split(' ')
    people = {}
    for i, line in enumerate(lines[3:]):
        likes = [int(x) for x in line.split(' ')[1:]]
        if i in people:
            people[i].update(likes)
        else:
            people[i] = set(likes)
        for j in likes:
            if j in people:
                people[j].update([int(i)])
            else:
                people[j] = set([int(i)])

    group_weights = []
    group_people_count = []
    groups = []
    visited = set()

    for current in people.keys():
        if current in visited:
            continue
        group = bfs(people, current)
        groups.append(group)
        group_people_count.append(len(group))
        group_weight = 0
        for i in group:
            group_weight += int(weights[int(i)])
        group_weights.append(group_weight)
        visited.update(group)

    dp = [[0 for x in range(m+1)] for y in range(len(groups))]
    for i in range(0, len(groups)):
        for j in range(m+1):
            if group_weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - group_weights[i]] + group_people_count[i])

    print(groups)
    print(group_weights)
    print(group_people_count)

    return str(dp[len(groups)-1][m])


if __name__ == '__main__':
    print(get_solution("28\n284\n140 65 149 18 75 174 87 94 8 70 136 51 41 169 182 106 141 127 9 17 108 107 89 181 86 159 111 195\n0\n0\n0\n1 4\n1 3\n1 6\n2 5 24\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n2 6 5\n0\n0\n0"))