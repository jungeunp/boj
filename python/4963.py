def dfs(matrix, y, x):
	dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
	queue = []
	queue.append((y,x))
	matrix[y][x] = 0
	
	while queue:
		cy, cx = queue.pop(0)
		
		for dy, dx in dirs:
			ny, nx = cy + dy, cx + dx
			if(ny >=0 and ny < h and nx >=0 and nx < w):
				if(matrix[ny][nx] == 1):
					queue.append((ny, nx))
					matrix[ny][nx] = 0
	

while True:
	w, h = map(int, input().split())
	if(w == 0 and h == 0):
		break
	
	matrix = [[0]*w for _ in range(h)]
	for i in range(h):
		temp = list(map(int, input().split()))
		for j in range(w):
			matrix[i][j] = temp[j]
	
	cnt = 0
	for i in range(h):
		for j in range(w):	
			if(matrix[i][j] == 1):
				cnt += 1
				dfs(matrix, i, j)
	
	print (cnt)
