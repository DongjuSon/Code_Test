import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

# DP =[[0] for i in range(N+1)]
DP = [10*7]*(10**6+1)
# DP[a] : a값을 연산하기에 가장 최소 방법
# print(DP)
 
DP[1] = 0
# DP[2] = 1
# DP[3] = 1
# a,b,c = 10**7, 10**7, 10**7
for i in range(2, 10**6+1):
    if i%3 == 0 :
        DP[i] = min(DP[i-1]*3, DP[i-1]+1)
    elif i%2 == 0 :
        DP[i] = min(DP[i-1]*2, DP[i-1]+1)
    else :
        DP[i] = min(DP[i], DP[i-1]+1)
    # DP[i] = min(a,b,c)

print(DP[N])
