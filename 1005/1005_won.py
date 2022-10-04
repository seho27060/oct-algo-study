# import math

def change(n, k):
    res = ""
    while n > 0:
        na = n % k
        mok = n // k
        n = mok
        res = str(na) + res
    return res

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    er = change(n, k)
    arr = er.split("0")
    for i in arr:
        if i == "":
            continue
        if isPrime(int(i)):
            # print(i)
            answer += 1
    return answer