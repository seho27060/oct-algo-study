def solution(n, k):
    # 자연수 n
    # k진수로 바꾼 수 -> 10진수로 봤을 때 prime number내 몇 개
    # p, p0, 0p, 0p0 -> 0 중심으로 split
    # 10진수일 때 0이 들어가지 않는 수
    def isPrime(val):
        if val <= 1: return False
        for num in range(2, int(val ** 0.5) + 1):
            if val % num == 0:
                return False
        return True
    
    
    def parseToK(val, k):  # val: number -> string
        if k == 10: return str(val)
        tmp = ''
        num = val
        while num >= k:
            tmp = str(num % k) + tmp
            num = num // k
        tmp = str(num) + tmp
        return tmp
    
    
    parsedNum = parseToK(n, k)
    splittedNum = parsedNum.split('0')
    
    answer = 0
    for strNum in splittedNum:
        if strNum == '': continue
        # if isPrime(int(strNum, k)):
        if isPrime(int(strNum)):
            answer += 1
    
    return answer
