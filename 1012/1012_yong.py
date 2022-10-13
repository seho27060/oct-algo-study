# 구현 문제??
# 가격을 저장할 리스트와 IN, OUT을 판단할 리스트 두개를 생성
# 출차될 때 주차했던 시간을 저장하고 모든 차량에 대해 출차처리를 진행한 뒤 가격을 측정
# defaultdict에서 value값만 출력하고 싶은데 생각한거랑 다르게 출력되는 이슈가 있어 정답용 리스트를 따로 만들었다.
from collections import defaultdict

def solution(fees, records):
    ans = []
    recordDic = defaultdict(int)
    price = defaultdict(lambda: 0)
    # 주차 시간 구하는 함수
    def cal1(i, o):
        return (int(o[:2]) * 60 + int(o[3:])) - (int(i[:2]) * 60 + int(i[3:]))
    # 요금 계산하는 함수
    def cal2(T):
        if T <= fees[0]:
            return fees[1]
        else:
            if (T - fees[0]) / fees[2] > (T - fees[0]) // fees[2]:
                return fees[1] + (((T - fees[0]) // fees[2]) + 1) * fees[3]
            else:
                return fees[1] + ((T - fees[0]) // fees[2]) * fees[3]

    for record in records:
        t, n, io = record.split(" ")
        if io == "IN":
            recordDic[int(n)] = t
        else:
            price[int(n)] += cal1(recordDic[int(n)], t)
            del recordDic[int(n)]
    for key in recordDic.keys():
        price[key] += cal1(recordDic[key], "23:59")

    for key in price.keys():
        price[key] = cal2(price[key])
    lst = sorted(price.items())
    for k, v in lst:
        ans.append(v)
    return ans