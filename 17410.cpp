#include <iostream>
using namespace std;

int matrix[101][101]; // 1-base
int num[101];
int copy_matrix[101];
int n = 3, m = 3;

void doR(){
	for(int i=1; i<=m; i++){ // 행마다 연산
		int end = 0; // matrix[i]배열의 원소 중(matrix[i][0]~matrix[i][n]) 가장 큰 값을 저장하는 변수 - 수 중 가장 큰 값
		for(int j=1; j<=n; j++){ // 해당 행의 모든 원소에 대해 연산
			num[matrix[i][j]]++; // matrix[0] 의 값이 121 이라면 차례대로 num[1]++ num[2]++ num[1]++ 해서 num[1]=2, num[2]=1이 되는 것
			if(matrix[i][j] > end)
				end = matrix[i][j]; // 100까지 다 안보고 중간에 루프 탈출하기 위해서 가장 큰 값을 넣어줌
		}

		int max_value = 0;
		for(int j=1; j<=end; j++){ // num 배열의 원소 중 가장 큰 값을 저장하는 변수 - 등장 횟수 중 가장 큰 값
			if(max_value < num[j])
				max_value = num[j];
		}

		int value = 1; // 등장횟수를 찾기 위한 변수
		int index = 0; // copy matrix에 저장하기 위한 인덱스 변수

		while(value <= max_value){ // value를 1부터 max_value까지 증가 시키면서 while문 반복 수행
			for(int j=1; j<=end; j++){ // 1~end까지 num[j] 보면서
				if(num[j] == value){ // 처음엔 num배열에 값이 1인 애들부터 copy_matrix를 채워감. j값이 1부터 시작하므로 숫자가 작은 것 부터 앞에 들어가게 됨
					copy_matrix[++index] = j; // 수
					copy_matrix[++index] = value; // 등장 횟수
					num[j] = 0; // 값을 옮긴 num배열은 0으로 초기화해줌
				}
			}
			value++; // 1증가시켜 다음 value(등장횟수)를 가진 수 탐색
		}
		if(index > n)
			n = index; // 가장 큰 index로 최대 행 크기를 바꾸어 줌

		for(int j=1; j<=n; j++){
			matrix[i][j] = copy_matrix[j]; // matrix(원본 배열)에 copy matrix를 복사
			copy_matrix[j] = 0; // copy matrix를 0으로 초기화해 다음 행에서 같은 작업을 할 수 있도록 함
		}

	}
}

void doC(){ // 연산 방법 doR과 같음 인덱스만 matrix[i][j] -> matrix[j][i], 카피할 때 범위만 n -> m
	for(int i=1; i<=n; i++){
		int end = 0;
		for(int j=1; j<=m; j++){
			num[matrix[j][i]]++;
			if(matrix[j][i] > end)
				end = matrix[j][i];
		}

		int max_value = 0;
		for(int j=1; j<=end; j++){
			if(max_value < num[j])
				max_value = num[j];
		}

		int value = 1;
		int index = 0;

		while(value <= max_value){
			for(int j=1; j<=end; j++){
				if(num[j] == value){
					copy_matrix[++index] = j;
					copy_matrix[++index] = value;
					num[j] = 0;
				}
			}
			value++;
		}

		if(index > m)
			m = index;

		for(int j=1; j<=m; j++){
			matrix[j][i] = copy_matrix[j];
			copy_matrix[j] = 0;
		}

	}
}

void printMatrix(){
	for(int i=1; i<=m; i++){
		for(int j=1; j<=n; j++){
			printf("%d ", matrix[i][j]);
		}
		printf("\n");
	}
}

int main() {
	int r, c, k;
	int cnt = 0;

	scanf("%d %d %d", &r, &c, &k);

	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			scanf("%d", &matrix[i][j]);
		}
	}

	while(matrix[r][c] != k){ // 행렬의 해당 인덱스에 k값이 있을 때 까지 while문 반복 수행
		if(cnt > 100){ // cnt가 100이 넘어가면 -1 출력하고 함수 종료
			cnt = -1;
			break;
		}

		if(m>=n){ // R연산
			doR();
		}
		else{ // C 연산
			doC();
		}
		cnt++;
	}

	printf("%d", cnt);
	return 0;
}
