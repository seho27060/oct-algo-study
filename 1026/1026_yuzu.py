def solution(places):
    answer = []
    for x in range(5):
        f = 0
        ans = 1
        for i in range(5):
            for j in range(5):
                if places[x][i][j] == 'P':
                    if 0 <= i < 4 and 0 <= j < 4 and places[x][i + 1][j + 1] == 'P':
                        if places[x][i + 1][j] != 'X' or places[x][i][j + 1] != 'X':
                            ans = 0
                            f = 1
                            break
                    if 0 <= i < 4 and 1 <= j < 5 and places[x][i + 1][j - 1] == 'P':
                        if places[x][i + 1][j] != 'X' or places[x][i][j - 1] != 'X':
                            ans = 0
                            f = 1
                            break
                    if 0 <= j < 4 and places[x][i][j + 1] == 'P':
                        ans = 0
                        f = 1
                        break
                    if 0 <= i < 4 and places[x][i + 1][j] == 'P':
                        ans = 0
                        f = 1
                        break
                    if 0 <= i < 3 and places[x][i + 1][j] != 'X' and places[x][i + 2][j] == 'P':
                        ans = 0
                        f = 1
                        break
                    if 0 <= j < 3 and places[x][i][j + 1] != 'X' and places[x][i][j + 2] == 'P':
                        ans = 0
                        f = 1
                        break

            if f == 1:
                break

        answer.append(ans)
    return answer