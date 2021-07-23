# 한 계단씩 오르기
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

step = []

for _ in range(N):
    a = int(input())
    step.append(a)

DP = [[0]*3 for _ in range(N+1)]

# 최대값 구할 때는 초기 DP값을 0으로 만든 뒤 입력 후 max
# DP[a][b] = a 계단 밟을 때 최대값
if N == 1 :
    print(step[0])
else :

    DP[0][0] = step[0]
    DP[1][0] = step[1]
    DP[1][1] = step[1]+DP[0][0]

    for i in range(2, N):
        DP[i][0] = step[i] + max(DP[i-2][0], DP[i-2][1])
        DP[i][1] = step[i] + DP[i-1][0]

    print(max(DP[N-1]))