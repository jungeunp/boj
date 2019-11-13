# 2798 블랙잭

# 3장 골라서 더해보기/백트래킹
def comb(num, start): # num:카드 갯수, start: 중복 방지하기 위한 시작 인덱스
	if(num == 3):
		sumlist.append(sum(temp)) # 카드 3장 조합이 만들어지면 합을 구함
		return
	
	for i in range(start, N):
		temp[num] = card[i]
		comb(num+1, i+1)
	

N, M = map(int, input().split())
card = list(map(int, input().split()))

temp = [0]*3 # 카드 3장을 저장할 임시 배열
sumlist = [] # 카드 3장의 합을 저장할 배열

comb(0, 0)

# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합 찾기
sumlist.sort() # 합 배열 정렬

if (sumlist[-1] < M): # 반례 잘 생각! 리스트의 값 중 M보다 큰 값이 없을 때 생각
	print (sumlist[-1])
else:
	answer_idx = 0
	for idx, val in enumerate(sumlist): # 리스트 돌면서 M 넘지 않는 최댓값 찾기
		if (val == M): # 정렬 되어 있으므로 M이 나오면 해당 값
			answer_idx = idx
			break
		elif (val > M): # 정렬 되어 있으므로 M을 넘는 값이 나올 때 직전의 값
			answer_idx = idx-1
			break
	print (sumlist[answer_idx])

