from collections import deque

# input
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


def solution(n, edge):
    # 그래프 연결
    graph = [[] for _ in range(n+1)]
    visit = [0] * (n+1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # bfs
    visit[1] = 1
    q = deque([1])

    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visit[next]:
                visit[next] = visit[x] + 1
                q.append(next)

    # output
    max_v = max(visit)  # 방문을 가장 많이 한 횟수
    cnt = visit.count(max_v)    # max_v번 만큼 방문한 노드의 개수

    # print(visit)
    # print(visit.count(max_v))
    return cnt if cnt > 0 else 1


print(solution(n, vertex))

