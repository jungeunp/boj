def cal(x, y, oper):
	if (oper == '+'):
		return x+y
	elif (oper == '*'):
		return x*y
	elif (oper == '-'):
		return x-y


def dfs(index, result): # backtracking - 모든 괄호 경우의 수 해보기
	global answer
	if (index > n-1):
		answer = max(result, answer)
		return
	
	if index == 0:
		oper = '+'
	else:
		oper = exp[index-1]

	if (index+2 < n): # 괄호로 묶기
		# 괄호로 묶은 앞
		temp = cal(int(exp[index]), int(exp[index+2]), exp[index+1])
		# 나머지 뒤
		dfs(index+4, cal(result, temp, oper))
	
	# 괄호로 안묶기
	dfs(index+2, cal(result, int(exp[index]), oper)) 
		

n = int(input())
exp = list(input())
answer = -1*10**10

dfs(0, 0)
print (answer)
