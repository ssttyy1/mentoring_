i = int(input()) #숫자 개수
l = list(map(int, input().split())) #정수 입력

max_num = 0 # 최대값 비교를 위한 변수
min_num = 1000001 # 최소값 비교를 위한 변수

for k in range(i): #최대값, 최소값 판별
    if l[k] > max_num:
        max_num = l[k]
    if l[k] < min_num:
        min_num = l[k]

print(min_num, max_num)