import sys
from sys import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dirR =[0,0,1,-1]
dirC =[1,-1,0,0]

N, M = map(int(input().split()))
visited = [[-1]*M for in range(N)]

cargo = [list(map(int, input().split())) for _ in range(N)]

que = deque()

for i in range(N):
    for j in range(M):
        if visited[i][j] == -1 :
            que.append([cargo[i][j], 0])

            while que :
                que.append([cargo[i][j], ])
                for k in range(4):
                    dirR[k] = que[1] + k
                    dirC[k] = que[1] + k
                    if dirR[k] >= 0 and dirR < N and dirC[k] >= 0 and dirC[k] < M :
                        if visited[i][j] == -1:
                    
                    
