# 개인정보 수집 유효기간
from sys import stdin


def solution(today, terms, privacies):
    t = list(map(int, today.split('.')))    # today를 연, 월, 일로 split

    # terms를 dictionary에 저장
    te_dict = {}
    for i in range(len(terms)):
        te_dict[terms[i][0]] = int(terms[i][2:])

    # privacies를 연, 월, 일, 유효기간으로 split
    p = []
    for i in range(len(privacies)):
        p.append([])
        p[i].append(int(privacies[i][0:4]))     # year
        p[i].append(int(privacies[i][5:7]))     # month
        p[i].append(int(privacies[i][8:10]))    # day
        p[i].append(privacies[i][11:12])        # validation date

    # 유효기간 계산
    validation = []
    for year, month, day, v in p:
        month += te_dict[v]
        day -= 1

        if day < 1:
            day = 28
            month -= 1

        while month > 12:
            month -= 12
            year += 1

        validation.append([])
        validation[-1].append(year)
        validation[-1].append(month)
        validation[-1].append(day)

    # 파기해야 할 개인정보 번호
    answer = []
    for i in range(len(validation)):
        # year 비교
        if validation[i][0] < t[0]:
            print("year", i, validation[i][0], t[0])
            answer.append(i+1)
            continue
        elif validation[i][0] == t[0]:
            # month 비교
            if validation[i][1] < t[1]:
                print("month", i, validation[i][1], t[1])
                answer.append(i+1)
                continue
            elif validation[i][1] == t[1]:
                # day 비교
                if validation[i][2] < t[2]:
                    print("day", i, validation[i][2], t[2])
                    answer.append(i+1)
                    continue

    return answer

    # print(t, "\n", te_dict, "\n", p, "\n")
    # return p


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))
# solution(today, terms, privacies)
