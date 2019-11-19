from functools import cmp_to_key
# 정렬 순서 
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

def mycmp(x, y):
	# x < y : 음수 리턴
	# x = y : 0 리턴
	# x > y : 양수 리턴 
	if(len(x) < len(y)): # 길이가 짧은 문자열이 앞 순서
		return -1
	elif(len(x) > len(y)): # 길이가 짧은 문자열이 앞 순서
		return 1 # y를 앞으로 보냄
	else: # 길이가 같을 경우
		if x < y: # x가 사전순으로 앞일 경우
			return -1
		else:
			return 1 # y를 앞으로 보냄
		
	
n = int(input())

text_list = set() # 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력(집합)
for _ in range(n):
	text_list.add(input())

text_list = list(text_list)
# text_list = sorted(text_list, cmp=mycmp)
# TypeError: 'cmp' is an invalid keyword argument for this function - python 2
# Use the key keyword and functools.cmp_to_key to transform your comparison function:
text_list = sorted(text_list, key=cmp_to_key(mycmp))

for i in text_list:
	print (i)
