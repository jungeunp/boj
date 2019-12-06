import copy

N = int(input())
M = int(input())

matrix = [[987654321]*(N+1) for _ in range(N+1)]
for i in range(N+1):
	matrix[i][i] = 0
	
for _ in range(M):
	from_v, to_v, cost = map(int, input().split())
	matrix[from_v][to_v] = min(cost, matrix[from_v][to_v])
		
answer = copy.deepcopy(matrix) # 값만 복사하기 위해 deepcopy 

for k in range(1, N+1):
	for i in range(1, N+1):
		for j in range(1, N+1):
			if (answer[i][k] + answer[k][j] < answer[i][j]):
				answer[i][j] = answer[i][k] + answer[k][j]

for i in range(N):
	for j in range(N):
		if answer[i+1][j+1] == 987654321:
			print("0", end=' ')
		else:
			print(answer[i+1][j+1], end=' ')
	print("")
