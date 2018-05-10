

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
    n, m = lines[0].split(' ')
    n, m = int(n), int(m)
    weights = lines[1].split(' ')
    people = {}
    for i, line in enumerate(lines[2:]):
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

    total_weight = 0
    dp = {}
    dp = [[0 for x in range(m)] for y in range(len(groups))]
    for i in range(1, len(groups)):
        for j in range(m):
            if group_weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - group_weights[i]] + group_people_count[i])

    print(str(dp[len(groups) - 1][m-1]))


if __name__ == '__main__':
    get_solution("5 5\n1 1 1 1 1\n1 1\n0\n0 1\n0\n0")