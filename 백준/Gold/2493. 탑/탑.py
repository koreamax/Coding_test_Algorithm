import sys

input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
s = [] # 인덱스를 담을 스택
cnt = [0] * N # 결과 저장 배열

# O(n) = 500,000
for i in range(N-1, -1, -1):
    # 스택에 값이 존재하고 다음 값이 top보다 클 때
    while s and top[s[-1]] < top[i]:
        cnt[s.pop()] = i+1 # cnt에 해당 인덱스 저장

    s.append(i)

print(*cnt)