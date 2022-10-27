dx = [1,-1,0,0]
dy = [0,0,-1,1]

def solution(places):
    answer = []

    def find(x,y):
        ST = [(x,y,0)]
        visit = [[0]*5 for _ in range(5)]
        visit[y][x] = 1
        while ST:
            nx,ny,cnt = ST.pop(0)
            for i in range(4):
                X = nx + dx[i]
                Y = ny + dy[i]
                if 0<=X<5 and 0<=Y<5 and visit[Y][X] == 0 and cnt+1<3 and t[Y][X] != 'X':
                    if t[Y][X] == 'P':
                        return 1
                    else:
                        ST.append((X,Y,cnt+1))
                        visit[Y][X]=1

    for t in places:
        s=0
        for y in range(5):
            for x in range(5):
                if t[y][x] == 'P':
                    if find(x, y):
                        answer.append(0)
                        s=1
                        break
            if s:
                break
        if s == 0:
            answer.append(1)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))