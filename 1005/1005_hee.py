# 소수
def prime_num(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


# k 진수
def func(n, k):
    ans = ''
    while n:
        ans = str(n % k) + ans
        n //= k
    return ans


# main
def solution(n, k):
    answer = 0
    x = func(n, k)
    L = len(x)
    i = 0
    while True:
        if L <= i:
            break

        if x[i] != '0':
            temp = x[i]
            while True:
                i += 1

                if L <= i:
                    break

                if x[i] != '0':
                    temp = temp + x[i]
                else:
                    break

            if prime_num(int(temp)):
                answer += 1
        else:
            i += 1

    return answer
