import sys
input = sys.stdin.readline
sys.setrecursionlimit(1100000)

N = int(input())

def solved(wei, DP):
  if wei < 0:
    return 987654321
  elif wei == 0:
    return 0
  if DP[wei] == -1:
    DP[wei] = 1+min(solved(wei-3, DP), solved(wei-5, DP))
  

  return DP[wei]


DP = [-1]*5005
# DP[a][b] : 무게가 b인 봉지를 추가했을 때 합 무게가 a가 될 최소 봉지 수

# DP[6] = DP[3] + 3 // DP[1] + 5

answer = solved(N, DP)
if answer >= 987654321:
  answer = -1
print(answer)