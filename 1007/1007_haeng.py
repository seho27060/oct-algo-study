def solution(gems):
    length = set(gems)
    visit = {}
    for i in length:
        visit[i] = 0
    s = 0
    e = len(gems)-1

    for i in gems:
        visit[i] += 1

    while 1:
        if visit[gems[e]] > 1:
            visit[gems[e]]-=1
            e -= 1
        else:
            break
    while 1:
        if visit[gems[s]] > 1:
            visit[gems[s]] -=1
            s +=1
        else:
            break

    answer = [s+1, e+1]
    while s<e and e< len(gems):
        if visit[gems[s]] > 1:
            visit[gems[s]] -= 1
            s += 1

        else:
            if e-s < answer[1] - answer[0]:
                answer = [s+1,e+1]
            if e < len(gems) -1 :
                e += 1
                visit[gems[e]] +=1
            else:
                break
    return answer


A = list(input().split())
print(solution(A))