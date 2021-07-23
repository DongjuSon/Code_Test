from collections import deque
import sys

M, N= map(int, sys.stdin.readline().split())
visited = [[-1]*M for _ in range(N)]
dirR = [0,0,-1,1]
dirC = [1,-1,0,0]

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

que = deque()

cnt_day = 0
# 초기값 세팅
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            que.append([i, j, 0])
            visited[i][j] = 1

while que :
    curr = que.popleft()
    cnt_day = max(cnt_day, curr[2])

    for i in range(4):
        nR = curr[0] + dirR[i]
        nC = curr[1] + dirC[i]
        if nR >= 0  and nR < N and nC >= 0 and nC < M :
            if visited[nR][nC] == -1 and tomato[nR][nC] == 0 :
                que.append([nR, nC, curr[2]+1])
                visited[nR][nC] = 1
                tomato[nR][nC] =1

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0 :
            cnt_day = -1

print(cnt_day)