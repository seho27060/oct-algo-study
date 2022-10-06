def solution(n, k):
    tmp = ''
    while n:
        tmp = str(n % k) + tmp
        n //= k

    ans = 0
    for num in tmp.split('0'):
        if num == "":
            continue
        elif num == "1":
            continue
        elif num == "2" or num == "3":
            ans += 1
        else:
            num = int(num)
            f = 0
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    f = 1
                    break
            if f == 0:
                ans += 1
    return ans