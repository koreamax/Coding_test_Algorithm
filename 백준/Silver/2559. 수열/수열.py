import sys

input = sys.stdin.readline

N, K = map(int, input().split())
T = list(map(int, input().split()))
s = [sum(T[:K])] # 슬라이딩 윈도우 만큼의 합 배열

# 윈도우 사이즈보다 큰 값을 넣어야 하니 인덱스 잘 생각할 것
for i in range(N-K):
    s.append(s[-1]-T[i]+T[K+i])

print(max(s))