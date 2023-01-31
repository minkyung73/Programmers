# 예상 대진표
import math


def power(n):
    cnt = 0
    while n != 1:
        n /= 2
        cnt += 1
    return cnt


def solution(n, a, b):
    cnt = power(n)

    for i in range(cnt):
        if math.ceil(a/2) == math.ceil(b/2):
            answer = i + 1
            break

        a = math.ceil(a/2)
        b = math.ceil(b/2)

    return answer


n = 8
a = 4
b = 7
print(solution(n, a, b))