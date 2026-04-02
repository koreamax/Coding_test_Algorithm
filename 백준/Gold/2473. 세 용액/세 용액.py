import sys

input = sys.stdin.readline

N = int(input())
l = sorted(list(map(int, input().split())))

m = sys.maxsize # 최솟값
answer = [0, 0, 0] # 정답

# O(n^2) = 5000 * 5000
for i in range(N-2): # i를 고정시키고 투포인터 이동 시키기
    start, end = i+1, N-1 # 투포인터 초기화
    while(start != end):
        sum = l[i] + l[start] + l[end]
        if (m > abs(sum)):
            m = abs(sum)
            answer[0:3] = l[i], l[start], l[end]
        
        if (sum > 0):
            end -= 1
        elif (sum < 0):
            start += 1
        else:
            print(*answer)
            exit(0)

print(*answer)