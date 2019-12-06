N = int(input())
M = int(input())

matrix = [[987654321]*(N+1) for _ in range(N+1)]

for i in range(N+1):
	matrix[i][i] = 0
	
for _ in range(M):
	from_v, to_v, cost = map(int, input().split())
	if matrix[from_v][to_v] > cost:
		matrix[from_v][to_v] = cost
		
for k in range(1, N+1):
	for i in range(1, N+1):
		if k == i:
			continue
		for j in range(1, N+1):
			if (matrix[i][k] + matrix[k][j] < matrix[i][j]):
				matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(1, N+1):
	for j in range(1, N+1):
		if matrix[i][j] == 987654321:
			print("0", end=' ')
		else:
			print(matrix[i][j], end=' ')
	print()
