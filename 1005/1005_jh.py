#진수 함수
def num(n, k) :
    result = ''
    while n >= k:
        a = n % k #나머지
        number = n // k #몫
        result += str(a)
        n = number
    result += str(n)
    return result[::-1]

#소수찾는 함수
def prime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True

def solution(n, k):
    ans = 0
    N = num(n, k)
    new = N.split('0')
    for i in range(len(new)):
        if new[i] == '':
            continue
        if prime(new[i]) == True:
            ans += 1
    return ans
