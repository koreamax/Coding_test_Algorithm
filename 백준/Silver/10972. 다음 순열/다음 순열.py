#next permutation 문제

from sys import stdin

N = int(stdin.readline())
li = list(map(int, stdin.readline().strip().split()))

for i in range(1, N):
    if (li[N-i] > li[N-i-1]): # 처음으로 오름차순인 부분 뒤에서부터 찾기
        for j in range(1, N - i + 1):
            if (li[N-j] > li[N-i-1]): # fir보다 큰 숫자 뒤에서부터 찾기
                li[N-j], li[N-i-1] = li[N-i-1], li[N-j] # swap
                li[N-i:N] = sorted(li[N-i:N]) # 재정렬
                print(*li)
                exit() # 내림차순이 아닐 떄 코드 출력 안 되도록

# 완전 내림차순
print(-1) 