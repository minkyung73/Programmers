from sys import stdin

def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]
    arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    arr[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [i, j] in puddles:
                arr[i][j] = 0
            else:
                arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000007
    return arr[n][m]


m = 4
n = 3
puddles = [[2, 2]]
# puddles = [[2, 2], [3, 2]]

print(solution(m, n, puddles))

