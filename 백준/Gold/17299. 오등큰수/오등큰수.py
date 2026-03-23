import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
F = [0] * 1000000 # 숫자 카운트 저장
NGF = [0] * N # 오등큰수
s = deque([0]) # 오등큰수의 인덱스

# O(n) = 1,000,000, 숫자 카운트 구하기
for i in range(N):
    F[A[i] - 1] += 1

# O(n) = 1,000,000
for i in range(1, N):
    # 카운트가 작을 때까지 pop한 값을 NGF에 삽입
    while s and F[A[s[-1]] - 1] < F[A[i] - 1]:
        NGF[s.pop()] = A[i]
    
    s.append(i)

while s: # 남은 것들은 큰 것들이므로 전부 -1
    NGF[s.pop()] = -1

print(*NGF)