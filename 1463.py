import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


X = int(input())

DP = [100000000]*(10**6+1)

DP[1] = 0
for i in range(1,1000001):
    if i*3 <= 1000000 :
        DP[i*3] = min(DP[i*3], DP[i]+1)
    if i*2 <= 1000000 :
        DP[i*2] = min(DP[i*2], DP[i]+1)
    if i+1 <= 1000000 :
        DP[i+1] = min(DP[i+1], DP[i]+1)
    


print(DP[X])
