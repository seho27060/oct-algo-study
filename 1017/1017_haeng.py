def solution(expression):
    global answer
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    L = []
    S = []
    ST = ''
    for i in expression:
        if i in num:
            ST += i
        else:
            L.append(ST)
            ST = ''
            L.append(i)
            S.append(i)
    L.append(ST)

    C = []
    ST = []

    def soonser(List):
        if len(ST) == len(List):
            C.append([])
            for j in ST:
                C[-1].append(j)
            return

        for i in List:
            if i not in ST:
                ST.append(i)
                soonser(List)
                ST.pop()

    soonser(set(S))
    def gogo(List, n, c):
        global answer
        ST = []
        if len(List) == 1:
            if abs(List[0]) > answer:
                answer = abs(List[0])
            return

        for i in range(len(List)):
            if List[i] == C[n][c]:
                last = ST.pop()
                if List[i] == '+':
                    ST.append(int(last) + int(List[i + 1]))
                elif List[i] == '-':
                    ST.append(int(last) - int(List[i + 1]))
                elif List[i] == '*':
                    ST.append(int(last) * int(List[i + 1]))
            elif i != 0 and List[i - 1] == C[n][c]:
                continue
            else:
                ST.append(List[i])
        gogo(ST, n, c + 1)

    answer = 0
    for k in range(len(C)):
        gogo(L, k, 0)

    return answer