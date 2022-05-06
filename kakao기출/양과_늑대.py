from itertools import permutations


def getRoute(s, p_tree):
    route = []
    while s != 0:
        s = p_tree[s]
        route.append(s)

    return route


def find(pos, sheep, wolf, visited, info):
    # 루트면
    if pos == 0:
        if visited[0] == 0:
            sheep += 1
            visited[pos] = 1
    else:
        # 늑대
        if info[pos] == 1 and visited[pos] == 0:
            wolf += 1
            visited[pos] = 1

        # 양
        elif info[pos] == 0 and visited[pos] == 0:
            sheep += 1
            visited[pos] = 1

    return sheep, wolf


def solution(info, edges):
    answer_list = []
    sheep_pos = []  # 루트를 제외한 양 위치
    tree = {}
    p_tree = {}  # 부모

    if sum(info) == 0:
        return len(info)

    for i in range(len(info)):
        if info[i] == 0 and i != 0:
            sheep_pos.append(i)

    # 양 방문 순서
    pmt = list(permutations(sheep_pos))
    # 트리 생성
    for edge in edges:

        if edge[0] in tree.keys():
            tree[edge[0]].append(edge[1])
        else:
            tree[edge[0]] = [edge[1]]

        if edge[1] in tree.keys():
            tree[edge[1]].append(edge[0])
        else:
            tree[edge[1]] = [edge[0]]

        if edge[1] in p_tree.keys():
            p_tree[edge[1]].append(edge[0])
        else:
            p_tree[edge[1]] = edge[0]

    # 양찾기
    for orders in pmt:

        visited = [0 for _ in range(len(info))]
        sheep = 0
        wolf = 0

        for order in orders:
            route = getRoute(order, p_tree)
            visited_tmp = visited
            wolf_tmp = wolf
            sheep_tmp = sheep
            route_len = len(route)
            for idx in range(route_len - 1, -1, -1):
                sheep, wolf = find(route[idx], sheep, wolf, visited, info)
            if sheep > wolf:
                if visited[order] == 0:
                    visited[order] = 1
                    sheep += 1
            else:
                visited = visited_tmp
                wolf = wolf_tmp
                sheep = sheep_tmp


        answer_list.append(sheep)

    answer = max(answer_list)

    return answer
