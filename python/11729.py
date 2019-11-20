def hanoi(num, start, mid, end):
	if (num == 1): # 원판이 한개만 남으면 start -> end 이동
		output.append((start, end))
		return
	else:
		hanoi(num-1, start, end, mid) # n-1개 원판을 start->mid 이동
		output.append((start, end)) # 제일 큰 원판을 start->end 이동
		hanoi(num-1, mid, start, end) # mid에 있던 n-1개 원판을 다시 end로 이동

n = int(input())

output = []
hanoi(n,1,2,3)

print (len(output)) # 배열의 크기가 수행 횟수
for x in output:
	print (x[0], x[1]) # (1,3) 형태로 저장되어있음-> x[0] x[1]로 출력
