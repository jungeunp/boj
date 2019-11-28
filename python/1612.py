N = input()

length = len(N)
ones = int('1'*length)
N = int(N)

# 곱해서 1만으로 이루어진 수가 안나오는 경우
# 2의 배수이거나, 5의 배수
if N % 2 is 0 or N % 5 is 0:
	print ("-1")
else:
	# 1의 자리수를 늘려가면서 나누는 방법 - 시간초과
	# 나머지를 활용해서 나눠가는 방법
	while True:
		if ones % N == 0:
			break
		else:
			ones = (ones % N)*10 + 1
			length += 1
			
	print (length)
	
# 11111 % 9901 = 1210 
# 111111 = (111110 + 1) / 111111 % 9901 = (1210*10+1) % 9901 = 2200
# 1111111 % 9901 = (2200*10+1) % 9901 = 2199
# 11111111 % 9901 = (2199*10+1) % 9901 = 2189