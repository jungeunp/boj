def DFS(node):
	if(visited[node] == 0):
		visited[node] = 1
		print (node+1, end=" ") # matrix의 index가 0-base 이므로 +1, print의 default end가 \n이므로 수정

		for val in adj_list[node]: # idx, val 둘 다 접근하기 위해 enumerate 사용
			if(visited[val] == 0): # 간선이 존재하고, 방문하지 않았다면
				DFS(val) # DFS 방문하기
		
def BFS(start):
	queue = [start]
	visited[start] = 1
	while queue:
		front = queue.pop(0)
		# 파이썬 list의 pop()은 리스트의 맨 마지막 요소를 반환하고 해당 요소를 삭제한다.
		# pop(idx)는 idx위치의 요소를 반환하고 삭제함
		
		print (front+1, end=" ") # matrix의 index가 0-base 이므로 +1, print의 default end가 \n이므로 수정

		for val in adj_list[front]:
			if(visited[val] == 0):
				visited[val]=1
				queue.append(val)

	
N, M, V = map(int, input().split()) 
# map 함수 map(적용시킬 함수, 적용할 요소들(list))
# list요소마다 int변환이 가능함

# 인접 리스트
adj_list = [[] for _ in range(N)] 
# [[0]*N] = [[0, 0, 0, 0]] / [[]*N] = [[]]
# 각각의 배열을 만들기 위해서는 반복문 사용해야 함
# adj_list = [[], [], [], []]

# 방문 행렬
visited = [0]*N

# 입력된 간선에따라 인접 행렬을 채움 - 입력으로 주어지는 간선은 양방향
for _ in range(M):
	src, dest = map(int, input().split())
	adj_list[src-1].append(dest-1)
	adj_list[dest-1].append(src-1)
	

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 인접 리스트를 정점 번호가 작은 순으로 정렬해줘야함
for nodes in adj_list:
	nodes = nodes.sort()


# DFS 수행 - 재귀/stack
DFS(V-1)
print ("")

# BFS 수행 - queue
visited = [0]*N # visited 배열 초기화
BFS(V-1)


