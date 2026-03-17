import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
NGE = [-1 for _ in range(N)]

d = [] # 인덱스 저장할 스택

for i in range(N):
    # 스택에 값이 존재하거나 새로 들어온 값이 top보다 클 때 까지 반복
    while d and A[d[-1]] < A[i]:
        # 오큰수에 저장
        NGE[d.pop()] = A[i]

    d.append(i) # 인덱스 추가

print(*NGE)