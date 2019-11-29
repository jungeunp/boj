def dfs(start, end, leng):
	global length
	if(start == end):
		length = leng
		return 
	if(visited[start] == False):
		visited[start] = True
		if not relations[start]:
			return
		else:
			for i in relations[start]:
				dfs(i, end, leng+1)

n = int(input())
q1, q2 = map(int, input().split())

visited = [False]*(n+1)

relations = [[] for i in range(n+1)]
m = int(input())
for _ in range(m):
	p, d = map(int, input().split())
	relations[p].append(d)
	relations[d].append(p)

length = -1
dfs(q1, q2, 0)

print (length)
