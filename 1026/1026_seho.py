# 221027 거리두기 확인하기
# n <= 5*5
# P - 자리/ O - 빈테이블/ X - 파티션
# 모든 P 자리에 맨해튼 2범위내 dfs?

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def solution(places):
    answer = []
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    for place in places:
        # for p in place:
        #     print(p)
        print("---")
        result = 1
        for row in range(5):
            for col in range(5):
                if place[row][col] == "P" and result:
                    stack = [[row,col]]
                    searchedSet = set()

                    while stack:
                        now = stack.pop()
                        searchedSet.add((now[0],now[1]))
                        for move in moves:
                            nxtR, nxtC = now[0] + move[0], now[1] + move[1]
                            if 0 <= nxtR < 5 and 0 <= nxtC < 5 and (nxtR,nxtC) not in searchedSet:
                                if (abs(row-nxtR)+abs(col-nxtC)) <= 2 and place[nxtR][nxtC] != "X":
                                    if place[nxtR][nxtC] == "O":
                                        stack.append((nxtR,nxtC))
                                    elif place[nxtR][nxtC] == "P":
                                        print(row,col,now,move,nxtR,nxtC)
                                        result = 0
                                        stack = []
                                        break
        answer.append(result)

    return answer

print(solution(places))