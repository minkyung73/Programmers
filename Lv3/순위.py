from collections import defaultdict

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]


def solution(n, edge):
    na_win = {}     # key가 value(들)을 이김
    na_lose = {}    # key가 value(들)한테 짐
    for i in range(n):
        na_win[i+1] = []
        na_lose[i+1] = []
    for a, b in edge:
        na_win[a].append(b)
        na_lose[b].append(a)

    # print(na_win)   # {1: [2], 2: [5], 3: [2], 4: [3, 2], 5: []}
    # print(na_lose)  # {1: [], 2: [4, 3, 1], 3: [4], 4: [], 5: [2]}

    for i in range(1, n+1):
        for winner in na_win[i]:    # i번 선수가 winner를 이김
            for winner2 in na_win[winner]:  # winner한테 진 선수는 i번 선수한테도 짐
                if i not in na_lose[winner2]:   # 중복 방지
                    na_lose[winner2].append(i)  # na_lose 딕셔너리에 추가

    for i in range(1, n+1):
        for loser in na_lose[i]:    # i번 선수가 winner를 이김
            for loser2 in na_lose[loser]:  # winner한테 진 선수는 i번 선수한테도 짐
                if i not in na_win[loser2]:     # 중복 방지
                    na_win[loser2].append(i)    # na_lose 딕셔너리에 추가

    # print(na_win)   # {1: [2, 5], 2: [5], 3: [2, 5], 4: [3, 2, 5], 5: []}
    # print(na_lose)  # {1: [], 2: [4, 3, 1], 3: [4], 4: [], 5: [2, 1, 3, 4]}

    answer = 0
    for i in range(1, n+1):
        if len(na_win[i]) + len(na_lose[i]) == n - 1:
            answer += 1

    return answer


print(solution(n, results))
