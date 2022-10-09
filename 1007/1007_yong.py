# 투포인터를 활용한 문제
# gems에 있는 보석들을 차례로 탐색하며 deque에 저장
# 처음에 set으로 해당 범위를 판단하여 모든 종료가 있는지 확인할 때는 시간초과가 발생
# defaultdict를 활용하여 중복성을 판단하니 시간초과가 해결됐음 

from collections import deque
from collections import defaultdict

def solution(gems):
    gemList = set(gems)
    l = 0
    r = 0
    check = deque()
    setCheck = defaultdict(lambda : 0)
    gap = 1000001
    while r <= len(gems):
        if r - l >= gap:
            val = check.popleft()
            setCheck[val] -= 1
            if setCheck[val] == 0:
                del setCheck[val]
            l += 1
            continue
        if len(setCheck) < len(gemList):
            if r == len(gems):
                break
            check.append(gems[r])
            setCheck[gems[r]] += 1
            r += 1
            continue
        if len(setCheck) == len(gemList):
            answer = [l+1, r]
            gap = r-l
            val = check.popleft()
            setCheck[val] -= 1
            if setCheck[val] == 0:
                del setCheck[val]
            l += 1
            continue
    return answer