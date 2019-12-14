N, M, T, K = map(int, input().split()) # N 가로 M 세로
treasure_x = [] # 리스트에 보석 위치 저장
treasure_y = []
answer, answer_x, answer_y = 0, 0, 0

for _ in range(T):
	x, y = map(int, input().split())
	treasure_x.append(x)
	treasure_y.append(y)

for idx in range(T): 
	# 각 꼭짓점 가로별 세로를 모두 대입해서 가장 금강석이 많은 지역 찾는 방법
	l_x = treasure_x[idx]
	r_x = l_x + K
	if (r_x > N): # 박스 길이가 지도보다 클 때 예외처리
		l_x -= (r_x - N)
		r_x = N # 제일 오른쪽에 맞추는 것
	
	for idx2 in range(T):
		t_y = treasure_y[idx2]
		b_y = t_y + K
		if(b_y > M):
			t_y -= (b_y - M)
			b_y = M
		
		count = 0 # 각 조합별 영역의 금강석 수
		
		for idx3 in range(T):
			# 범위 체크
			if( (treasure_x[idx3] >= l_x and treasure_x[idx3] <= r_x) and (treasure_y[idx3] >= t_y and treasure_y[idx3] <= b_y)):
				count += 1
			
		if(answer < count):
			answer = count
			answer_x = l_x
			answer_y = b_y 
			
print (answer_x, answer_y)
print (answer)
