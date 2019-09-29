#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Point{
	int x, y;
};

int n, m, can_num=0, result=0;

int matrix[8][8];
int copy_matrix[8][8]; // 바이러스 퍼트리기 위한 copy

vector <Point> candidates; // 벽 후보 위치
vector <int> visited; // 벽 후보 중 3개를 뽑기 위한 visited 배열
vector <Point> v(3); // 벽 후보(3개 조합)

queue <Point> virus; // 바이러스 위치
int dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; // 바이러스를 퍼트리기 위한 방향


void diffuse(){ // 바이러스를 퍼트리는 함수
	int count = 0; // 안전 영역의 넓이
	queue <Point> temp = virus; // virus 위치 복사

	for(int i=0; i<n; i++){ // 매트릭스 복사
		for(int j=0; j<m; j++){
			copy_matrix[i][j] = matrix[i][j];	
		}
	}

	for(int i=0; i<3; i++){ // 벽 후보(3개 조합)위치에 벽 세워줌
		copy_matrix[v[i].x][v[i].y] = 1;
	}
	
	while(!temp.empty()){ // bfs - 바이러스 퍼트리기
		Point current = temp.front();
		temp.pop();
		
		for(int i=0; i<4; i++){
			int next_x = current.x + dir[i][0];
			int next_y = current.y + dir[i][1];
			if(next_x>=0 && next_x <n && next_y>=0 && next_y < m){
				if(copy_matrix[next_x][next_y] == 0){ // 벽이 아닐 때만 퍼트릴 수 있음
					copy_matrix[next_x][next_y] = 2;
					temp.push({next_x, next_y}); // 바이러스가 퍼진 곳을 큐에 넣어줌
				}
			}
		}
	}
	
	for(int i=0; i<n; i++){ // 안전 영역 계산
		for(int j=0; j<m; j++){
			if(copy_matrix[i][j] == 0) 
				count++;
		}
	}
	if(result < count)
		result = count; // max 함수 안쓰고 직접 비교함, 써도 됨
}

void permutation(int num, int start){ // 중복을 제거하기 위해서 start 지정
	if(num == 3){ // 벽 3개가 다 세워졌을 때 바이러스 퍼트리는 함수 호출
		diffuse();
	}
	else{
		for(int i=start; i<can_num; i++){ 
			if(!visited[i]){
				visited[i] = 1;
				v[num] = candidates[i]; // 벡터 day인덱스에 좌표 갱신
				permutation(num+1, i+1); // 다음 후보는 나보다 큰 좌표에서만 - 중복 제거
				visited[i] = 0;
			}
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);
	
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			scanf("%d", &matrix[i][j]);
			if(matrix[i][j] == 0){
				candidates.push_back({i, j});
				can_num++;
			}
			else if(matrix[i][j] == 2){
				virus.push({i, j});
			}
		}
	}
	visited.resize(can_num, 0); // visited 벡터 resize
	
	permutation(0, 0); // num = 0, start = 0으로 호출
	
	printf("%d", result);
	
	return 0;
}
