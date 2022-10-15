import math

def solution(fees, records):
    answer = []

    history = dict()
    basicT, basicF, unitT, unitF = fees

    endtime = 60*23 + 59

    for i in records:
        time, number, state = i.split()
        number = int(number)
        h, m = map(int, time.split(':'))
        newtime = 60*h + m

        if number not in history:
            history[number] = [[newtime, state]]
        else:
            history[number].append([newtime, state])

    sorted_history = sorted(history.items())
    for key, value in sorted_history:
        result = 0
        for i in value:
            if i[1] == "OUT":
                result += i[0]
            else:
                result -= i[0]

        if value[-1][1] == "IN":
            result += endtime


        if result <= basicT:
            answer.append(basicF)
        else:
            ans = basicF + math.ceil((result-basicT) / unitT) * unitF
            answer.append(ans)

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))