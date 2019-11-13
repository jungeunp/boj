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
answer = 0

for val in sumlist: # 리스트 돌면서 M 넘지 않는 최댓값 찾기
	if (val > answer and val <= M):
		answer = val
		
print (answer)
