n = []

while True:
    a = int(input())
    if a == 0:
        break

    n.append(a)

m = max(n)

prime = [True for _ in range(2*m + 1)]
prime[0:2] = [False] * 2

for i in range(2, int((2*m)**(0.5))+1):
    for j in range(i*i, 2*m + 1, i):
        prime[j] = False

for i in range(len(n)):
    cnt = 0
    for j in range(n[i] + 1, 2*n[i] + 1):
        if prime[j] == True:
            cnt += 1
    print(cnt)