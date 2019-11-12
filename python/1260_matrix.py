def DFS(node):
	if(visited[node] == 0):
		visited[node] = 1
		print (node+1, end=" ") # matrix의 index가 0-base 이므로 +1, print의 default end가 \n이므로 수정

		for idx, val in enumerate(adj_matrix[node]): # idx, val 둘 다 접근하기 위해 enumerate 사용
			if(val == 1 and visited[idx] == 0): # 간선이 존재하고, 방문하지 않았다면
				DFS(idx) # DFS 방문하기
		
def BFS(start):
	queue = [start]
	visited[start] = 1
	while queue:
		front = queue.pop(0)
		# 파이썬 list의 pop()은 리스트의 맨 마지막 요소를 반환하고 해당 요소를 삭제한다.
		# pop(idx)는 idx위치의 요소를 반환하고 삭제함
		
		print (front+1, end=" ") # matrix의 index가 0-base 이므로 +1, print의 default end가 \n이므로 수정

		for idx, val in enumerate(adj_matrix[front]):
			if(val == 1 and visited[idx] == 0):
				visited[idx]=1
				queue.append(idx)

	
N, M, V = map(int, input().split()) 
# map 함수 map(적용시킬 함수, 적용할 요소들(list))
# list요소마다 int변환이 가능함

# 인접 행렬
adj_matrix = [[0]*N for _ in range(N)] 
# [[0]*N for i in range(N)] i 변수 필요 없으니까 _로 주기
# adj_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 방문 행렬
visited = [0]*N

# 입력된 간선에따라 인접 행렬을 채움 - 입력으로 주어지는 간선은 양방향
for _ in range(M):
	src, dest = map(int, input().split())
	adj_matrix[src-1][dest-1] = 1 # matrix의 index가 0-base 이므로 -1
	adj_matrix[dest-1][src-1] = 1
	
# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고
# 더 이상 방문할 수 있는 점이 없는 경우 종료

# DFS 수행 - 재귀/stack
DFS(V-1)
print ("")


# BFS 수행 - queue
visited = [0]*N # visited 배열 초기화
BFS(V-1)

