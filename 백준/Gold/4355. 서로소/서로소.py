import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: # n = 0일 때 끝
        break
    elif n == 1: # n = 1일 때 0 출력
        print(0)
        continue

    i = 2
    answer = n
    while i < int(n**0.5) + 1: # 소인수분해, O(N**0.5)
        valid = False # 중복 계산 제거
        while n % i == 0:
            n //= i
            if not valid: # 오일러 피
                answer -= answer // i
                valid = True
        i += 1

    if n != 1: # 마지막 남은 소수가 1이면 사용 안 함
        answer -= answer // n
    print(answer) 