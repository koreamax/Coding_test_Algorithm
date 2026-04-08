N = int(input())

if N == 1:
    print(0)
    exit(0)

prime = [True for _ in range(N+1)]
prime[0:2] = [False] * 2
#에라토스테네스의 체 만들기
for i in range(2, int(N**(0.5)) + 1):
    for j in range(i*i, N+1, i):
        prime[j] = False

num = []
for i in range(2, N+1):
    if prime[i] == True:
        num.append(i)

#투 포인터, 슬라이딩 윈도우 시작
start, end = 0, 0
tmp = num[start]
cnt = 0

while (end != len(num)):
    if tmp <= N:
        if (tmp == N):
            cnt += 1

        end += 1

        if end < len(num):
            tmp += num[end]
    else:
        tmp -= num[start]
        start += 1

print(cnt)