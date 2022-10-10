import math

def n_number(n, k):
    val = ''
    while n > 0:
        val = str(n %k) +val
        n = n // k
    return val

def is_prime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False

    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True




def solution(n, k):
    answer = 0
    k_num = n_number(n,k)
    for i in k_num.split('0'):
        if i == '':
            continue
        elif is_prime(int(i)):
            answer+=1
    return answer