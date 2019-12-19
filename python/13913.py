start, end = map(int, input().split())
visit = [0]*100001
queue = []
queue.append((start, 0))
visit[start] = 1

end_time, path_cnt = -1, 0

while True:
	loc, step = queue.pop(0)
	
	if(step == end):
		break
	
	if(loc-1 >= 0 and visit[loc-1] == 0):
		if(loc-1 == end):
			if(end_time < 0):
				end_time = step+1
				path_cnt += 1
			elif(end_time == step+1):
				path_cnt += 1
		else:
			queue.append((loc-1, step+1))
			visit[loc-1] = 1
	if(loc+1 <= 100000 and visit[loc+1]==0):
		if(loc+1 == end):
			if(end_time < 0):
				end_time = step+1
				path_cnt += 1
			elif(end_time == step+1):
				path_cnt += 1
		else:
			queue.append((loc+1, step+1))
			visit[loc+1] = 1
	if(loc*2 <= 100000 and visit[loc*2]==0):
		if(loc*2 == end):
			if(end_time < 0):
				end_time = step+1
				path_cnt += 1
			elif(end_time == step+1):
				path_cnt += 1
		else:
			queue.append((loc*2, step+1))
			visit[loc*2] = 1

print (end_time)
print (path_cnt)
