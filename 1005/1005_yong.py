# 소수 찾기 문제
# 처음에는 에라토스테네스의 체를 사용했는데 런타임에러 발생, 그냥 0을 스플릿한 숫자를 바로바로 판별하는 방법으로 변경
# 1번 테스트 시간초과가 발생해 찾아보니 while문의 조건을 변경해서 해결

def solution(n, k):
    ans = 0
    def isPrime(num):
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    def trans(n, k):
        result = ''
        while n > 0:
            q, r = divmod(n, k)
            result = str(r) + result
            n = q
        return result
    lst = trans(n, k).split("0")
    for i in lst:
        if i != '' and i != '1':
            if isPrime(int(i)):
                ans += 1
    return ans


solution(437674, 3)