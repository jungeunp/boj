import math # floor, sqrt 사용을 위해 math 모듈 사용

m = int(input())
n = int(input())

answer = []
sum_num = 0

for i in range(m, n+1):
	if math.floor(math.sqrt(i)) == math.ceil(math.sqrt(i)): 
		# math.sqrt 결과가 소수점이므로 floor, ceil 값을 이용해 자연수인지 확인
		answer.append(i)
		sum_num += i
		
if len(answer) == 0: # 리스트가 비어있는 경우, 즉 범위 안에 완전 제곱수가 없는 경우
	print (-1)
else:
	print (sum_num) # 완전 제곱수의 합
	print (answer[0]) # 가장 작은 완전 제곱수
