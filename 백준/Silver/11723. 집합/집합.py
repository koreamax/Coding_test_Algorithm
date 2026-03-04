from sys import stdin

M = int(stdin.readline())
S = set()

for _ in range(M):
    pre = list(stdin.readline().strip().split())
    if len(pre) == 2:
        sec = int(pre[1])

    if (pre[0] == "add"):
        S.add(sec)
    elif (pre[0] == "remove"):
        S.discard(sec)
    elif (pre[0] == "check"):
        print(1 if sec in S else 0)
    elif (pre[0] == "toggle"):
        if sec in S:
            S.discard(sec)
        else:
            S.add(sec)
    elif (pre[0] == "all"):
        S = {i+1 for i in range(20)}
    elif (pre[0] == "empty"):
            S = set()