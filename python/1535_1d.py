N = int(input())

pain = list(map(int, input().split()))
gain = list(map(int, input().split()))	

dp = [0]*100 # 인덱스에 해당하는 체력으로 가질수 있는 가장 큰 행복을 저장

for i in range(N):
	for j in range(99, pain[i]-1, -1):
		# dp[99] ~ dp[현재 인덱스 체력]
		# dp[체력] = max(같은 체력에 현재 인덱스 안 포함한 행복, 현재 인덱스 포함해서 깎인 체력에 현재 인덱스 포함한 행복 )
		dp[j] = max(dp[j], dp[j-pain[i]]+gain[i]) # 현재 인덱스 포함 or 불포함 정하는 것
		
print (dp[99])
