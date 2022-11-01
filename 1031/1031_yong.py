# 효율성은 카페가서 다시 도전하겠읍니다...

def solution(info, query):
    answer = []
    dic = {
        'cpp' : [],
        'java' : [],
        'python' : [],
        '-' : []
    }
    for _ in info:
        l, p, e, f, s = _.split()
        dic[l].append((p, e, f, int(s)))
        dic['-'].append((p, e, f, int(s)))

    for i in query:
        cnt = 0
        l, a1, p, a2, e, a3, f, s = i.split()
        s = int(s)
        for j in dic[l]:
            if p != '-' and p != j[0]:
                continue
            if e != '-' and e != j[1]:
                continue
            if f != '-' and f != j[2]:
                continue
            if j[3] < s:
                continue
            cnt += 1
        answer.append(cnt)
    print(answer)


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])