def solution(idx, heal):
	temp = 0
	if (idx == N):
		return 0
	unselected = solution(idx+1, heal) # 현재 인덱스 포함 안하는 경우
	selected = 0 # 현재 인덱스를 포함하면 체력 바닥나서, 포함 못하는 경우
	if heal >= pain[idx]: # 현재 인덱스 포함 가능한 경우
		selected = solution(idx+1, heal-pain[idx]) + gain[idx]
	
	return max(unselected, selected)
	
N = int(input())

pain = list(map(int, input().split()))
gain = list(map(int, input().split()))	

heal = 99
idx = 0

print (solution(idx, heal))


