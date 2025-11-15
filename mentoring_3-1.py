n = int(input()) # 숫자 개수
l = list(input()) # 입력 받고 더해질 수
sum = 0

for i in range(n): # 숫자 더하기
    sum += int(l[i])

print(sum)