# 괄호 회전하기
from sys import stdin


def solution(s):
    new_s = []
    for i in range(len(s)):
        new_s.append(s[i:]+s[:i])

    # 올바른 괄호 문자열인지 확인
    answer = []
    for i in new_s:
        stack = []
        if i[0] in [']', '}', ')']:
            i = i[1:]
            answer.append("X")
            continue

        # for j in i:
        #     if stack:
                # if j=='(' or j=='{' or j=='[':





    return new_s


s = stdin.readline().strip()
# print(solution(s))


