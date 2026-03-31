import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort() # O(nlogn)
start = 0 # 투 포인터
end = n - 1 # 투 포인터
cnt = 0 # 합이 x가 되는 수

# start = end이면 끝내기
while (start != end):
    # 같으면 cnt 추가
    if (a[start] + a[end] == x):
        cnt += 1
        start += 1
    # 작으면 start가 작은것이므로 추가
    elif (a[start] + a[end] < x):
        start += 1
    # 크다며 end가 큰 것이므로 추가
    else:
        end -= 1

print(cnt)