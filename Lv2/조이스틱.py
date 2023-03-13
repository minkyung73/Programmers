def solution(name):
    cnt = 0
    move = len(name) - 1

    cursor = 0
    init_name = "A" * len(name)

    for idx, alphabet in enumerate(name):
        # 상하 이동
        cnt += min(ord(alphabet)-ord('A'), 1 + ord('Z') - ord(alphabet))

        # 좌우 이동
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        move = min([move, 2 * idx + len(name) - next, idx + 2 * (len(name) -next)])

    cnt += move
    return cnt


print(solution("JEROEN"))

