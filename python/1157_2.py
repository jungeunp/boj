# 1157_2.py
# 미리 알파벳 dict를 만들어줌

str = input().upper() # 입력받아 대문자로 변환
str_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0,
          'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

max_char = '' # 가장 많이 등장한 알파벳을 저장할 변수
cnt = 0 # 등장 횟수의 중복 횟수를 저장할 변수

for i in str:
	str_dict[i] += 1 # 알파벳을 key로 가지면, value를 1 증가
	

for k, v in str_dict.items():
	if v == max(str_dict.values()): # value값이 dict value의 최댓값과 같으면
		max_char = k # max_char에 key 할당
		cnt += 1 # 중복을 체크하기 위해 cnt 변수 증가
		
if(cnt == 1): # max값이 하나면, 가장 많이 사용된 알파벳이 하나만 존재하면 해당 알파벳 출력
	print(max_char)
else: # 가장 많이 사용된 알파벳이 여러 개면 ? 출력
	print('?')
		
