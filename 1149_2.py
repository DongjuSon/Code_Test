import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solved(N, color, DP, RGB):
    # solved == N층에 color칠 했을 때의 최소비용 리턴
    if N == 0 :
        return 0
    if DP[N][color] == -1 :
        cage = [10**6+1]*3
        for i in range(3):
            if i != color:
                cage[i] = solved(N-1, i, DP, RGB)

        DP[N][color] = RGB[N-1][color] + min(cage)
    return DP[N][color]

N = int(input())
DP = [[-1]*3 for _ in range(1001)]
# DP[a][b] == a행 집에 b색깔을 칠했을 때의 최소비용이 들어가는 곳 

RGB = [list(map(int, input().split())) for _ in range(N)]

print(min(solved(N, 0, DP, RGB), solved(N, 1, DP, RGB), solved(N, 2, DP, RGB)))


