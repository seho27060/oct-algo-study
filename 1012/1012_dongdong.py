import math


def changeTime(start, end):  # 분 환산 함수
    h1, m1 = map(int, start.split(':'))
    h2, m2 = map(int, end.split(':'))
    total1 = h1 * 60 + m1
    total2 = h2 * 60 + m2

    return total2 - total1


def solution(fees, records):
    dtime, dfee, utime, ufee = fees
    check = {}  # 차량 체크 딕셔너리
    check_time = {}  # 차량 시간 체크 딕셔너리

    # in - out이 모두 있을 경우
    for rec in records:
        time, num, inout = rec.split()
        if inout == "IN":
            check[num] = time

        else:
            if num not in check_time:
                check_time[num] = changeTime(check[num], time)
            else:
                check_time[num] += changeTime(check[num], time)
            check[num] = "0"

    # 끝나는 시간을 나가는 시간으로 간주하는 차량
    for key, value in check.items():
        if value != "0":  # 나감 체크 없을 경우
            if key in check_time:
                check_time[key] += changeTime(value, "23:59")
            else:
                check_time[key] = changeTime(value, "23:59")

    check_time = sorted(check_time.items())

    answer = []
    for num, total_time in check_time:
        if total_time <= dtime:  # 기준시간 미초과
            answer.append(dfee)
        else:
            answer.append(dfee + math.ceil((total_time - dtime) / utime) * ufee)

    return answer