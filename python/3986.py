# 3986.py

n = int(input())
cnt = 0

for _ in range(n):
	words = input()
	length = len(words)
	
	stack_list = []
	
	for i in range(length): # 인덱스 접근을 위해 range 사용
		if(stack_list == []): 
			# 반례) AABB - AA가 없어지면 stack이 비어서 IndexError 발생 
			stack_list.append(words[i])
		else:
			if(stack_list[-1] == words[i]): # 스택의 top과 현재 원소 같을 때 top 원소 pop
				stack_list.pop() # == stack_list.pop(-1)
			else: # 아닐 경우 현재 원소 스택에 넣어줌
				stack_list.append(words[i]) 
	
	if(stack_list == []): # for문 종료 후 stack이 비었으면 다 짝이 맞은 것
		cnt += 1

print (cnt)	
