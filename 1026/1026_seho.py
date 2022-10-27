# 221027 거리두기 확인하기
# n <= 5*5
# P - 자리/ O - 빈테이블/ X - 파티션
# 모든 P 자리에 맨해튼 2범위내 dfs?

# 원래 코드
def solution(places):
    answer = []
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    for place in places:
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
                                        result = 0
                                        stack = []
                                        break
        answer.append(result)

    return answer

# Clean Code?
def solution(places):

    answer = []

    for place in places:
        result = 1
        seachPoints = []

        for row in range(5):
            for col in range(5):
                if place[row][col] == "P":
                    startPoints.append((row,col))

        for point in startPoints:
            if result:
                result = checkDistanceFrom(point,place)
            else:
                break

        answer.append(result)
    return answer

def checkDistanceFrom(start,place):
    stack = [[start[0], start[1]]]
    searchedSet = set()
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    distanceCheck = 1

    while stack:
        now = stack.pop()
        searchedSet.add((now[0], now[1]))
        for move in moves:
            nxtR, nxtC = now[0] + move[0], now[1] + move[1]
            if isPointInSearchRange((nxtR,nxtC)) and isPointNotInSearchedSet((nxtR,nxtC),searchedSet):
                if manhattanDistance(start,(nxtR,nxtC)) <= 2:
                    if place[nxtR][nxtC] == "X":
                        continue
                    elif place[nxtR][nxtC] == "O":
                        stack.append((nxtR, nxtC))
                    elif place[nxtR][nxtC] == "P":
                        distanceCheck = 0
                        stack = []
                        break
    return distanceCheck

def isPointInSearchRange(point):
    return 0 <= point[0] < 5 and 0 <= point[1] < 5

def isPointNotInSearchedSet(point,searchedSet):
    return point not in searchedSet

def manhattanDistance(departure, arrival):
    return abs(departure[0] - arrival[0]) + abs(departure[1] - arrival[1])
