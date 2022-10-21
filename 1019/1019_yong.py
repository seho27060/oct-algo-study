# 슬라이딩 윈도우 방식을 활용해 큐를 나눴을 때 합이 같아지는 범위를 찾는다
# 그 상황에서 큐를 움직이는 횟수를 구해 기존 답안보다 적다면 답으로 넣는다.
def solution(queue1, queue2):
    answer = -1

    def check(l, r):
        global answer
        q = len(queue) - 1
        q1 = len(queue1) - 1
        if r < q1:
            return (r+1) + len(queue2) + l
        elif r == q1:
            return l
        elif r < q:
            return (r-q1) + l
        # r == q
        else:
            if l <= q1:
                return (r-q1) + l
            else:
                return l - q1


    result = (sum(queue1) + sum(queue2)) // 2
    queue = queue1 + queue2
    l = r = 0
    val = queue[0]
    while r < len(queue):
        if val < result:
            r += 1
            if r < len(queue):
                val += queue[r]
            else:
                break
        elif val > result:
            val -= queue[l]
            l += 1
        else:
            cnt = check(l, r)
            if answer == -1:
                answer = cnt
            else:
                if cnt < answer:
                    answer = cnt
            r += 1
            if r < len(queue):
                val += queue[r]
            else:
                break
    return answer

solution([1, 1], [1, 5])