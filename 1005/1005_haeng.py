def checknum(N):
    for i in range(2,int(N**0.5)+1):
        if N%i ==0:
            return 0
    return 1

def solution(n, k):
    change = ''
    while n >= k:
        change += str(n % k)
        n = n // k
    change += str(n)
    K = change[::-1]
    result = []
    s=0
    A = ''
    for j in range(len(K)):
        if K[j] == '0':
            if s == 0 and A:
                result.append(int(A))
                A = ''
                s=1

            B = ''
            for k in range(j+1,len(K)):
                if K[k] == '0':
                    break
                else:
                    B += str(K[k])
            if B:
                result.append(int(B))
        else:
            if s==0:
                A+= K[j]
    if A:
        result.append(int(A))

    answer = 0
    for i in result:
        if i >1 and checknum(i):

            answer+=1
    return answer


n = int(input())
k = int(input())
print(solution(n,k))