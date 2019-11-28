def eat_fish(y, x, shark_size):
    answer = 0
    q = []
    dir_y = [-1,0,0,1]
    dir_x = [0,-1,1,0]
    
    eat = 0
    visited = [[0]*n for _ in range(n)]
    q.append((0,y,x)) # y, x, dist
    
    while(q):
        q.sort()
        now_dist, now_y, now_x = q.pop(0)
        if(0 < matrix[now_y][now_x] < shark_size): # 잡아먹을 수 있을 때
            matrix[now_y][now_x] = 0
            eat += 1
            answer += now_dist
            now_dist = 0
            q = []
            visited = [[0]*n for _ in range(n)]
            if (eat == shark_size):
                shark_size += 1
                eat = 0
    
        #else 잡아 먹을 수 없을 때는 지금 위치에서 이동 - 잡아 먹고서 하는 행동과 같음
        for i in range(4):
            next_y = now_y + dir_y[i]
            next_x = now_x + dir_x[i]
            if(next_y < 0 or next_y >= n  or next_x < 0 or next_x >= n):
                continue
            if(visited[next_y][next_x] or 0 < matrix[next_y][next_x] > shark_size): # 방문했거나 상어보다 크거나
                continue
            visited[next_y][next_x] = 1
            q.append((now_dist+1, next_y, next_x))

    print (answer)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(matrix[i][j] == 9):
            matrix[i][j] = 0
            eat_fish(i, j, 2)

