from sys import stdin

M = int(stdin.readline())
S = set()

for _ in range(M):
    pre = list(stdin.readline().split())
    cmd = pre[0]
    if len(pre) == 2:
        sec = pre[1]
        n = int(sec)
        if n in S:
            a = True
        else:
            a = False

    if (cmd == "add"):
        if not a:
            S.add(n)
    elif (cmd == "remove"):
        if a:
            S.remove(n)
    elif (cmd == "check"):
        if a:
            print(1)
        else:
            print(0)
    elif (cmd == "toggle"):
        if a:
            S.remove(n)
        else:
            S.add(n)
    elif (cmd == "all"):
        S = set()
        for i in range(20):
            S.add(i+1)
    elif (cmd == "empty"):
            S = set()