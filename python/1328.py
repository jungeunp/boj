def check_building(temp):
    global answer
    #증가하는 수열
    left = 0
    right = 0
    temp_max = 0
    for t in temp:
        if(temp_max < t):
            left += 1
            temp_max = t

    if not left == L:
        return
    else:
        temp_max = 0
        for i in range(len(temp)-1, 0, -1):
            if(temp_max < temp[i]):
                right += 1
                temp_max = temp[i]

        if right == R:
            answer += 1
        else:
            return


def permutate(N, cnt):
    if (cnt == N):
        check_building(temp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            temp[cnt] = buildings[i]
            permutate(N, cnt+1)
            visited[i] = False


N, L, R = map(int, input().split())

buildings = [i for i in range(1, N+1)]
visited = [False]*N
temp = [0]*N
answer = 0
permutate(N, 0)
print (answer)
