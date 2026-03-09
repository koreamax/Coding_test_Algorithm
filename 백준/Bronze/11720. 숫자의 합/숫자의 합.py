from sys import stdin

N = int(stdin.readline())

arr = list(map(int, stdin.readline().strip())) # 공백 문자 없애기

print(sum(arr))