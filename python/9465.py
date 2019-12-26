tc = int(input())
for _ in range(tc):
	n = int(input())
	
	matrix = []
	for _ in range(2):
		matrix.append(list(map(int, input().split())))
		
	dp = [[0]*100000 for _ in range(3)]
	
	dp[0][0] = matrix[0][0]
	dp[1][0] = matrix[1][0]
	dp[2][0] = 0
	
	for i in range(1, n):
		dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + matrix[0][i]
		dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + matrix[1][i]
		dp[2][i] = max(dp[0][i-1], dp[1][i-1])
	
	result = max(dp[0][n-1], dp[1][n-1])
	result = max(result, dp[2][n-1])
	
	print (result)
		
