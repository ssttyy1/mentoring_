people = int(input()) #사람 수
time = list(map(int, input().split())) #걸리는 시간
time.sort(reverse = False) #오름차순 정리
sum, waut = 0, 0
wait_and_use_time = [] #한 사람당 (대기 + 이용)시간

for i in range(people):
    waut += time[i]
    wait_and_use_time.append(waut)
    sum += wait_and_use_time[i]

print(sum)