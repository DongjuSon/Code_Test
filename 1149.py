import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
DP = [[10**6+1]*3 for _ in range(1001)]
# DP[a][b] == a행 집에 b색깔을 칠했을 때의 최소비용이 들어가는 곳 

RGB = [list(map(int, input().split())) for _ in range(N)]

DP[0][0] = RGB[0][0]
DP[0][1] = RGB[0][1]
DP[0][2] = RGB[0][2]

for i in range(1, N):
    DP[i][0] = RGB[i][0]+min(DP[i-1][1], DP[i-1][2])
    DP[i][1] = RGB[i][1]+min(DP[i-1][0], DP[i-1][2])
    DP[i][2] = RGB[i][2]+min(DP[i-1][1], DP[i-1][0])
    
print(min(DP[N-1]))