#include <iostream>
#include <algorithm> // max를 위한 헤더파일

using namespace std;

// 인덱스 1-base -> 1000+1로 선언
int t[1001];
int p[1001];
int dp[1001];

int main() {
	int n;
	scanf("%d", &n);

	for(int i=1; i<=n; i++){ // 인덱스 1-base로 받음
		scanf("%d %d", &t[i], &p[i]);
	}

	for(int i=n; i>0; i--){ // 마지막날부터 채우기
		if(i+t[i] <= n+1) // 기간 내 할 수 있는 일인지 체크
			dp[i] = max(dp[i+1], dp[i+t[i]]+p[i]);
			// 해당 날의 일을 했을 때, 하지하고 넘어갈 때 최댓값 비교
		else
			dp[i] = dp[i+1]; // 기간 내에 못할 경우 해당날 공백, 다음날의 dp값 가져옴
	}

	printf("%d", dp[1]);
	return 0;
}
