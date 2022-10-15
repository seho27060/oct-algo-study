# 프로그래머스 k진수에서 소수 개수 구하기

# 소수판정 - 에라토스테네스 체 사용

def solution(n, k):
    # 진법변환
    ans = ""
    while n:
        ans = str(n % k) + ans # 나머지를 계속 뒤에다 가져다 붙여야 됨
        n = n // k

    ans = ans.split("0")    # 0을 기준으로 쪼개기

    answer = 0
    for x in ans:
        if len(x) == 0: # 빈 공간시 건너뛰기
            continue
        if int(x) < 2:  # 0 또는 1일 경우 건너뛰기
            continue

        is_prime = True
        for i in range(2, int(int(x) ** 0.5) + 1):  # 소수판정 범위
            if int(x) % i == 0:
                is_prime = False
                break

        if is_prime:
            answer += 1

    return answer




