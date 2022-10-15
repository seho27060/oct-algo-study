# 프로그래머스 보석쇼핑

def solution(gems):
    gem = dict()
    gemNum = len(set(gems))  # 보석 수

    l, r = 0, 0 # 두 포인터 모두 0에서 시작, 두 포인터 안에 보석이 모두 안담기면 r을, 담기면 l을 오른쪽으로 이동

    gem[gems[0]] = 1
    answer = [0, len(gems)]

    while l < len(gems) and r < len(gems):  # 범위내
        # 딕셔너리에 보석 종류가 모두 담기면
        if len(gem) == gemNum:
            if r - l < answer[1] - answer[0]:  # 범위가 더 좁다면
                answer = [l, r] # 정답 갱신
            gem[gems[l]] -= 1  # 포인터에 있는 보석 딕셔너리에서 빼주기 => 다음 포인터로 이동했을때 체크를 위해

            if gem[gems[l]] == 0:
                del gem[gems[l]]    # 보석이 0이 되면 키도 없어야 해서 아예 지워버리기
            l += 1  # 모든 보석 종류 확인 되었으면 l 오른쪽으로 이동해서 더 작은 배열 가능한지 찾기

        # 안담기면 r을 오른쪽으로 이동
        else:
            r += 1
            if r == len(gems):  # r이 범위 넘어가면 멈춰
                break
            if gems[r] in gem:  # 있으면 더해주기
                gem[gems[r]] += 1
            else:   # 없으면 딕셔너리에 새롭게 추가
                gem[gems[r]] = 1

    return [answer[0] + 1, answer[1] + 1]

