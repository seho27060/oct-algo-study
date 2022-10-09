def solution(gems):
    N = len(set(gems))
    L = len(gems)

    answer = [1, L+1]
    start, end = 0, 0
    D = {}

    while end < L:
        if gems[end] not in D:
            D[gems[end]] = 1
        else:
            D[gems[end]] += 1

        if len(D) == N:
            while start <= end:
                if 1 < D[gems[start]]:
                    D[gems[start]] -= 1
                    start += 1

                else:
                    if end - start < answer[1] - answer[0]:
                        answer = [start+1, end+1]
                    break
        end += 1
    return answer
