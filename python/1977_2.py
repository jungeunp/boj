# math 모듈 사용하지 않고 
# 범위 안의 자연수를 제곱해서 범위안에 존재하는지 확인하는 코드
# floor, ceil 쓸 필요 없기 때문에 4ms 정도 빠름

m = int(input())
n = int(input())

answer = []
sum_result = 0

for i in range(1, n):
    if m <= i**2 <= n:
        answer.append(i**2)
        sum_result += i**2
    elif i**2 > n:
    	break

if len(answer) == 0: # answer == [] 로도 비교 가능
    print(-1)
else:
    print(sum_result)
    print(answer[0])
