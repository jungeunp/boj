def calc_building(N, L, R):
    dp[1][1][1] = 1

    for n in range(2, N+1): # 빌딩 갯수
        for l in range(1, L+1): # 왼쪽에서 보이는 빌딩 갯수
            for r in range(1, R+1):
                dp[n][l][r] = (dp[n-1][l][r]*(n-2) + dp[n-1][l-1][r] + dp[n-1][l][r-1])%1000000007

    print (dp[N][L][R])

N, L, R = map(int, input().split())
#dp = [[[0 for k in range(R+1)] for j in range(L+1)] for i in range(N+1)] - 런타임 에러
dp = [[[0]*101 for i in range(101)] for j in range(101)]

calc_building(N, L, R)
