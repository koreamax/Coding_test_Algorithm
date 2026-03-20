import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

D = deque() #(index, value)

# O(n) = 5,000,000
for i in range(N):
    if D and D[0][0] <= i-L: # D에도 남아있으면 없애주기, 0보다 큰 인덱스에는 존재할 수 없음
        D.popleft()
    
    #넣어준 값이 얼마나 최솟값인지 확인
    while D and A[i] < D[-1][1]:
        D.pop()

    D.append([i, A[i]])

    print(D[0][1], end=" ")