# 221013 주차 요금 계산
import math

def solution(fees, records):
    answer = []
    carsDict = {}

    for record in records:
        getTime, number, order = record.split()
        if order == "IN":
            if number not in carsDict.keys():
                carsDict[number] = [getTime,0]
            else:
                carsDict[number] = [getTime,carsDict[number][1]]
        elif order == "OUT":
            startHour, startMinute = map(int,carsDict[number][0].split(":"))
            getHour, getMinute = map(int,getTime.split(":"))
            result = (getHour-startHour)*60 + (getMinute-startMinute)
            carsDict[number] = ["0",carsDict[number][1]+result]
    # print(carsDict)


    result = []
    for carNum, TimeAndRate in carsDict.items():
        carTime, carRate = TimeAndRate
        # print(carNum,carRate)
        if carTime != "0":
            getHour, getMinute = map(int,carTime.split(":"))
            carRate = carRate + (23 - getHour) * 60 + (59 - getMinute)

        rate = fees[1]
        if carRate > fees[0]:
            rate += math.ceil((carRate-fees[0])/fees[2])*fees[3]
        result.append([int(carNum),rate])
    result.sort(key=lambda x:x[0])

    for res in result:
        answer.append(res[1])

    return answer


print(solution(frees,records))