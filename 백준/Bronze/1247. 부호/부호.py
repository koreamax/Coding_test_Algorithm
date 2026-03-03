from sys import stdin

for _ in range (3):
    N = int(stdin.readline())
    li = [int(stdin.readline()) for _ in range(N)]

    if sum(li) > 0:
        print("+")
    elif sum(li) < 0:
        print("-")
    else:
        print(0)