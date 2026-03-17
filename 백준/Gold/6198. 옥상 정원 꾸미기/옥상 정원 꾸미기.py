N = int(input())

H = [int(input()) for _ in range(N)]
H.append(1000000001) # 마지막 빌딩을 위한 장치

cnt = [0] * N # 확인 가능한 옥상 수
s = [] # 인덱스를 넣을 스택

for i in range(N+1):
    # s가 존재하고 다음 인덱스의 값이 더 크거나 같으면 반복
    while s and H[s[-1]] <= H[i]:
        # top 인덱스의 빌딩 개수 채워주기
        tmp = s.pop()
        cnt[tmp] = i-tmp-1

    s.append(i)

print(sum(cnt))