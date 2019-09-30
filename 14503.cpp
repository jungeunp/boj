#include <iostream>
using namespace std;

struct Point{
	int y, x, d;
}; // y=row, x=column

int n, m;
int count=0;
int map[50][50];

int dir[4][2] = {{-1,0}, {0,1}, {1,0}, {0,-1}}; // 0북 1동 2남 3서
// 북->서->남->동 +3%4
// 북 반대 남 0->2 / 2->0 / 1->3 / 3->1 +2%4

void clean(Point robot);
void explore(Point robot, int sum);

void explore(Point robot, int sum){
	//printf("%d %d %d\n", robot.y, robot.x, robot.d);
	if(sum == 4){ // 네 방향 다 살펴봤을 때
		Point opposite;
		// 북 반대 남 0->2 / 2->0 / 1->3 / 3->1 +2%4
		opposite.y = robot.y + dir[(robot.d+2)%4][0];
		opposite.x = robot.x + dir[(robot.d+2)%4][1];
		
		// 후진할 수 없는 경우
		if(map[opposite.y][opposite.x] == 1){
			return;
		}
		else{
			opposite.d = robot.d; // 바라보는 방향 유지
			explore(opposite, 0);
		}
	}
	else{
		Point next;
		// 북->서->남->동 +3%4
		next.y = robot.y + dir[(robot.d+3)%4][0];
		next.x = robot.x + dir[(robot.d+3)%4][1];
	
		if(map[next.y][next.x] == 0){
			next.d = (robot.d+3)%4;
			clean(next);
		}
		else if(map[next.y][next.x] == -1 || map[next.y][next.x] == 1){
			robot.d = (robot.d+3)%4; // 로봇위치에서, 로봇 방향만 바꾸기
			explore(robot, sum+1); // 여기서 틀렸음! next 위치로 넘기면 안되고 robot위치 넘겨야함
		}
		
	}
}

void clean(Point robot){
	map[robot.y][robot.x] = -1; // 청소 완료면 -1값 넣어줌
	count++; 	
	explore(robot, 0); // 해당 위치부터 새로운 탐색 시작
}

int main() {
	Point robot;
	int zero=0;
	scanf("%d %d", &n, &m);
	
	scanf("%d %d %d", &robot.y, &robot.x, &robot.d);
	
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			scanf("%d", &map[i][j]);
		}
	}

	clean(robot);
	
	printf("%d", count);
	return 0;
}
