# 답을 바로 계산하는 최적의 방법을 찾을 수 없을 때는
# 가능한 경우의 수 중 조건을 만족하는 답 찾기

buttons = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
channel = int(input())
n = int(input())

if (n == 0): # 고장난 버튼이 없을 때, 바로 해당 채널로 갈 수 있음
	pass
else:
	#broken = map(int, input().split())
	# set 자료구조 (집합) 사용시 집합간 뺄셈(차집합) 가능
	broken = set(input().split()) 
	buttons -= broken
	
min_move = abs(channel - 100) # + 혹은 - 로만 채널을 이동하는 횟수

# 최소값 - 숫자 입력이 후 연산자로 이동, 연산자는 둘 중 하나만 사용  
# 목표 숫자보다 크거나, 작거나 두 가지 경우

# 이동하려는 채널의 범위 (0 ≤ N ≤ 500,000) 
# 가능한 채널의 범위는 (0 ≤ N ≤ 1,000,000) 내려가는 경우도 포함
# 모든 숫자에 대해 가능 여부를 체크하고, 가장 차이가 적게 나는 숫자 저장

for num in range(1000001):
	flag = True
	for n in str(num): # 숫자 한 자릿수씩 보기
		if(n not in buttons): # or if n not in buttons
			flag = False
	if(flag): # 조합이 가능한 숫자일 경우
		#if (min_move > len(str(num)) + abs(channel-num)):
		#	min_move = len(str(num)) + abs(channel-num)
		# len(str(num)) + abs(channel-num) = 해당 숫자 누르는 횟수 + ++/--로 이동하는 횟수
		min_move = min(min_move, len(str(num))+abs(channel-num))

print (min_move)
