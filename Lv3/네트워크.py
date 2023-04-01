# dfs/bfs
# Union find
from collections import deque

def solution(n, computers):
    answer = 0
    graph = {}

    # 그래프 그리기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            elif computers[i - 1][j - 1] == 1:
                if not i in graph:
                    graph[i] = [j]
                else:
                    graph[i].append(j)

    # 네트워크 개수 세기
    visited = []
    for root in range(1, n+1):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                queue += set(graph[node]) - set(visited)
                print(queue)

    return graph


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))

# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
# root_node = 1
#
# from collections import deque
#
#
# def BFS_with_adj_list(graph, root):
#     visited = []
#     queue = deque([root])
#
#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             queue += graph[n] - set(visited)
#             print("graph[n]:", graph[n], "\tvisited:", visited, "\tqueue:", queue)
#     return visited
#
#
# print(BFS_with_adj_list(graph_list, root_node))

