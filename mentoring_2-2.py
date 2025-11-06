N = int(input())
original_N = N
count = 0

while (1):
    ten = int(N / 10)
    one = int(N % 10)
    plus_ten_one = ten + one
    N = (one * 10) + (plus_ten_one % 10)
    count += 1
    if original_N == N:
        break

print(count)