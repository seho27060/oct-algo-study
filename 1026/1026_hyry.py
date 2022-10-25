def isValid(newRow, newCol):
    if 0 <= newRow < 5 and 0 <= newCol < 5:
        return True
    return False


def checkDistanceOne(place, row, col):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        newR, newC = row + dr, col + dc
        if not isValid(newR, newC): continue
        if place[newR][newC] == 'P':
            return False
    return True


def checkDistanceTwo(place, row, col):
    posToCheck =  {
        (-2, 0): [(-1, 0)],
        (-1, -1): [(-1, 0), (0, -1)],
        (-1, 1): [(-1, 0), (0, 1)],
        (0, -2): [(0, -1)],
        (0, 2): [(0, 1)],
        (1, -1): [(1, 0), (0, -1)],
        (1, 1): [(1, 0), (0, 1)],
        (2, 0): [(1, 0)]
    }
    
    for dr, dc in posToCheck.keys():
        newR, newC = row + dr, col + dc
        if not isValid(newR, newC) or place[newR][newC] != 'P': continue
        for subDr, subDc in posToCheck[(dr, dc)]:
            subNewR, subNewC = row + subDr, col + subDc
            # if not isValid(subNewR, subNewC): continue
            if place[subNewR][subNewC] != 'X':
                return False
    return True
    
    
def solution(places):
    '''
         2             
       2 1 2
     2 1 0 1 2    
       2 1 2  
         2
    '''
    answer = []
    
    for place in places:
        
        badDistance = False
        for row in range(5):
            if badDistance: break 
            for col in range(5):
                if place[row][col] != 'P': continue
                if not checkDistanceOne(place, row, col) or\
                    not checkDistanceTwo(place, row, col):
                    answer.append(0)
                    badDistance = True
                    break
        else:
            if not badDistance:  # 여기서 체크 한번 더 안 하면 테스트 22 틀림
                answer.append(1)
                
    return answer
    