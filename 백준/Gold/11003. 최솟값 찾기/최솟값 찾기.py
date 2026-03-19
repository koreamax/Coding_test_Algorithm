import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

D = deque() #(index, value)
window = deque() # 윈도우 슬라이딩 인덱스 저장

# O(n) = 5,000,000
for i in range(N):
    window.append(i)
    if len(window) == L + 1: # 윈도우 사이즈 넘치면 빼기
        tmp = window.popleft() # 윈도우 하나 빼주기
        if D[0][0] == tmp: # D에도 남아있으면 없애주기, 0보다 큰 인덱스에는 존재할 수 없음
            D.popleft()
    
    #넣어준 값이 얼마나 최솟값인지 확인
    while D and A[i] < D[-1][1]:
        D.pop()

    D.append([i, A[i]])

    print(D[0][1], end=" ")