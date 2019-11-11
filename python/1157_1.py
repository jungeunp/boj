# 1157_1.py
# 미리 알파벳 dict를 만들지 않고 있는 알파벳으로만 만들어줌

str = input().upper() # 입력받아 대문자로 변환

str_dict = {} # dict형 사용
max_char = '' # 가장 많이 등장한 알파벳을 저장할 변수
cnt = 0 # 등장 횟수의 중복 횟수를 저장할 변수

for i in str:
	if i in str_dict: # 이미 key가 존재하면 value를 1 증가
		str_dict[i] += 1
	else: # key가 존재하지 않으면 dict에 key를 추가함, value는 1로
		str_dict[i] = 1

# str_dict 예시
# 입력 Misisippi -> str_dict {'M': 1, 'I': 4, 'S': 4, 'P': 1}
# 입력 zZa -> str_dict {'Z': 2, 'A': 1}


for k, v in str_dict.items():
	if v == max(str_dict.values()): # value값이 dict value의 최댓값과 같으면
		max_char = k # max_char에 key 할당
		cnt += 1 # 중복을 체크하기 위해 cnt 변수 증가
		
if(cnt == 1): # max값이 하나면, 가장 많이 사용된 알파벳이 하나만 존재하면 해당 알파벳 출력
	print(max_char)
else: # 가장 많이 사용된 알파벳이 여러 개면 ? 출력
	print('?')
		
