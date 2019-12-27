N, M = map(int, input().split())
matrix = []
for _ in range(N):
	matrix.append(list(map(int, input().split())))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[1][1] = matrix[0][0]

for i in range(2, N+1):
	dp[i][1] = dp[i-1][1] + matrix[i-1][0]

for i in range(2, M+1):
	dp[1][i] = dp[1][i-1] + matrix[0][i-1]

for i in range(2, N+1):
	for j in range(2, M+1):
		dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]

T = int(input())
for _ in range(T):
	sy, sx, ey, ex = map(int, input().split())
	print (dp[ey][ex]-dp[ey][sx-1]-dp[sy-1][ex]+dp[sy-1][sx-1])
