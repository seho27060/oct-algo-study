def solution(fees, records):
    answer = []
    dic = dict()
    for i in records:
        lst = i.split(' ')
        time = lst[0].split(':')
        if lst[1] in dic.keys():
            dic[lst[1]].append(time)
        else:
            dic[lst[1]] = [time]
    time_dic = dict()
    car_num = []
    for num in dic.keys():
        car_num.append(num)
        time_lst = dic[num]
        if len(time_lst) % 2 == 0:
            for k in range(len(time_lst) - 1, -1, -2):
                out_time = int(time_lst[k][0]) * 60 + int(time_lst[k][1])
                in_time = int(time_lst[k - 1][0]) * 60 + int(time_lst[k - 1][1])

                if num in time_dic.keys():
                    time_dic[num] += out_time - in_time
                else:
                    time_dic[num] = out_time - in_time
        else:
            for k in range(len(time_lst) - 1, -1, -2):
                if k == len(time_lst) - 1:
                    out_time = 23 * 60 + 59
                    in_time = int(time_lst[k][0]) * 60 + int(time_lst[k][1])
                    time_dic[num] = out_time - in_time
                else:
                    out_time = int(time_lst[k + 1][0]) * 60 + int(time_lst[k + 1][1])
                    in_time = int(time_lst[k][0]) * 60 + int(time_lst[k][1])
                    time_dic[num] += out_time - in_time

    car_num.sort()
    for i in car_num:
        cost = fees[1]
        time = time_dic[i]
        print(time)
        if time <= fees[0]:
            answer.append(cost)
        else:
            if (time - fees[0]) % fees[2] == 0:

                cost += (time - fees[0]) // fees[2] * fees[3]
            else:
                cost += ((time - fees[0]) // fees[2] + 1) * fees[3]
            answer.append(cost)

    return answer