def get_district(visited, y, x, num): # bfs 
	cnt = 0
	dir = [[-1,0], [1,0], [0,-1], [0,1]]
	queue = []
	visited[y][x] = 1
	queue.append((y,x))

	while(queue): # queue == [] 사용하지 말기
		now = queue.pop(0) # 첫번째 원소 pop - front

		for k in range(4):
			next_y = now[0]+dir[k][0]
			next_x = now[1]+dir[k][1]
			
			if(next_y < 0 or next_y >= n or next_x < 0 or next_x >= n): # 다음 좌표가 matrix 범위 내인지 확인
				continue
			if(visited[next_y][next_x] == 1): # 이미 방문한 좌표인지 확인
				continue
			if(matrix[next_y][next_x] <= num): # 기준 num보다 높이가 낮다면
				visited[next_y][next_x] = 1 # 방문하고 pass
				continue
			
			visited[next_y][next_x] = 1 # 같은 안전 영역에 포함됨
			queue.append((next_y, next_x)) # 큐에 넣어줌
			

n = int(input())
matrix = []
max_num = 0
answer = 0

for i in range(n):
	matrix.append(list(map(int, input().split())))
	if max_num < max(matrix[i]):
		max_num = max(matrix[i])
	
for k in range(0, max_num):
	visited = [[-1]*n for _ in range(n)] # 방문 배열 매번 초기화
	district = 0

	for i in range(n):
		for j in range(n):
			if(visited[i][j] is -1 and matrix[i][j] > k):
				district += 1
				get_district(visited, i, j, k)

	if (answer < district):
		answer = district
		
print (answer)
