n, k = map(int, input().split())
coin = []

for _ in range(n):
	tmp = int(input())
	coin.append(tmp)
	
dp = [100001]*(k+1) 
# 1원 동전으로 목표 금액 100,000를 만드는 동전의 갯수는 100,000 
# 초기값을 100,000보다 1이 큰 100,001로 설정
dp[0] = 0 
# 1원 동전으로 목표 금액 1을 만드는 동전의 갯수 0

for c in coin:
	for idx in range(c, k+1): # 비교 범위 i번째 동전~ 목표 금액으로 비교 횟수를 줄임
		dp[idx] = min(dp[idx-c]+1, dp[idx])
		
if(dp[k] == 100001):
	dp[k] = -1

print (dp[k])
