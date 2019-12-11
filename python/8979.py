N, K = map(int, input().split())
medal = dict()
for _ in range(N):
	temp = list(map(int, input().split()))
	medal[temp[0]] = (temp[1], temp[2], temp[3])

ordered_medal = dict(sorted(medal.items(), key=(lambda x:x[1]), reverse=True))

idx = 0
num = 1
now = (-1, -1, -1)
for key, value in ordered_medal.items():
	if(now == value):
		num += 1
	else:
		idx += num
		num = 1
		now = value
	if(key == K):
		print (idx)
		break
	
