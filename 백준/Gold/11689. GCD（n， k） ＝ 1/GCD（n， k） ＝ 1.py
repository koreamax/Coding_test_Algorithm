n = int(input())

if n == 1 or n == 2:
    print(1)
    exit(0)

prime = []
answer = n

i = 2
# O(n**0.5) = 10**6
for i in range(2, int(n**(0.5)) + 1): # 소인수분해
    while n % i == 0:
        n //= i
        if i not in prime: # 굳이 있으면 넣지 않음
            prime.append(i)

if n != 1: # n = 1일 때 넣을 필요 없음
    prime.append(n)

for i in range(len(prime)): # 오일러피 
    answer -= answer // prime[i]

print(answer)