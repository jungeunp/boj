#include <iostream>
#include <algorithm> // max를 위한 헤더파일

using namespace std;

int n, max_result = 0;
// 인덱스 1-base -> 15+1로 선언
int t[16];
int p[16];

void dfs(int day, int sum){ // 해당 날에 일을 하는지, 일을 안 하는지
	if(day == n+1){ // 일을 끝내야하는 날짜에 도달하면 max값 갱신
		max_result = max(max_result, sum);
	}
	else{
		if(day+t[day] <= n+1) // 일을 하는 경우 - 끝나는 날짜가 정해진 기간 안인지 확인
			dfs(day+t[day], sum+p[day]); // day에 마치는 시간, sum에 현재 날짜의 이득 넣어줌
		dfs(day+1, sum); // 일을 안하는 경우 - 현재까지 sum으로 다음날로 점프
	}
}

int main() {
	scanf("%d", &n);

	for(int i=1; i<=n; i++){ // 인덱스 1-base로 받음
		scanf("%d %d", &t[i], &p[i]);
	}

	dfs(1, 0);

	printf("%d", max_result);
	return 0;
}
