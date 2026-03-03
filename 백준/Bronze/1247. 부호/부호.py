max_int = 9223372036854775807

for i in range(3):
    sum = 0
    cnt = 0
    N = int(input())
    for j in range(N):
        sum += int(input())
        if (sum >= max_int):
            sum -= max_int
            cnt += 1
        elif (sum <= -max_int):
            sum += max_int
            cnt -= 1

    sum += cnt * max_int

    if sum > 0:
        print("+")
    elif sum < 0:
        print("-")
    else:
        print("0")