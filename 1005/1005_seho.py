#221008 k진수에서 소수 개수 구하기

def solution(n, k):
    answer = 0
    result = ""

    # k진수로 만들기 그냥 몫, 나머지로 구하면 됨
    while n >= k:
        n,a = divmod(n,k)
        result = str(a) + result
    result = str(n) + result

    primeNumSet = []

    # k진수로 변환된 result를 처음부터 훑으면서 조건 만족하는 정수 찾기
    start = 0
    while start < len(result):
        if result[start] != "0":
            for end in range(start,len(result)):
                if result[end] == "0":
                    if result[start:end] != "1":
                        primeNumSet.append(result[start:end])
                    start = end
                    break
            else:
                if result[start:] != "1":
                    primeNumSet.append(result[start:])
                start = len(result)

        else:
            start += 1

    primeNumSet = list(primeNumSet)

    # 조건을 만족하는 정수들 중 소수 찾기
    for num in primeNumSet:
        check = True
        if int(num) >= 2:
            for idx in range(2,int(int(num)**0.5)+1):
                if int(num)%idx == 0:
                    check = False
                    break
            if check:
                answer += 1
    return answer

print(solution(n,k))
