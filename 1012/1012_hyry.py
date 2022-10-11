from math import ceil


def parseRecord(record):
    wholeTime, carNum, inOut = record.split()
    hour = int(wholeTime[:2])
    minute = int(wholeTime[3:])
    
    wholeMinute = hour * 60 + minute
    
    return wholeMinute, carNum, inOut


def calculateFee(basicTime, basicFee, timeUnit, unitFee, timeDiff):
    overTime = timeDiff - basicTime
    
    if overTime <= 0:
        return basicFee
    
    if overTime > 0:
        return basicFee + ceil(overTime / timeUnit) * unitFee
    

def solution(fees, records):
    # 입차, 출차
    # 차랑별 주차 요금 계산
    # 출차 기록이 없다면 23:59으로 계산
    # 7 * 60 = 420 - 180 = 240
    # fees: 기본 시간, 기본 요금, 단위 시간, 단위 요금
    # records [1, 1_000] 시각 차량번호 내역
    carsIn = dict()
    carsTime = dict()
    carsFee = dict()
    
    basicTime, basicFee, timeUnit, unitFee = fees
    
    for record in records:
        minute, carNum, inOut = parseRecord(record)
        if inOut == 'IN':
            carsIn[carNum] = minute
        if inOut == 'OUT':
            inTime = carsIn[carNum]
            timeDiff = minute - inTime
            carsTime[carNum] = carsTime.get(carNum, 0) + timeDiff
            del carsIn[carNum]
    
    # 23:59분에 나간 차들
    lastMin = 23 * 60 + 59
    for carNum, inTime in carsIn.items():
        timeDiff = lastMin - inTime
        carsTime[carNum] = carsTime.get(carNum, 0) + timeDiff
    
    for carNum, accTime in carsTime.items():
        calculatedFee = calculateFee(basicTime, basicFee, timeUnit, unitFee, accTime)
        carsFee[carNum] = calculatedFee
        
        
#             print(carNum, timeDiff)
#             # 요금 계산
#             calculatedFee = calculateFee(basicTime, basicFee, timeUnit, unitFee, timeDiff)
#             # 요금 계산한 것을 carsFee에 넣기
#             carsFee[carNum] = carsFee.get(carNum, 0) + calculatedFee
#             # 계산한 차는 지우기
#             del cars[carNum]
    
#     # for 문 이후에도 남아있는 차량들 = 23:59 처리
#     lastMin = 23 * 60 + 59
#     for carNum, inTime in cars.items():
#         timeDiff = lastMin - inTime
#         calculatedFee = calculateFee(basicTime, basicFee, timeUnit, unitFee, timeDiff)
#         carsFee[carNum] = carsFee.get(carNum, 0) + calculatedFee
    
    answer = list(map(lambda x: x[1], sorted(carsFee.items())))
    return answer
