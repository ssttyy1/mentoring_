N_10, B_2_36 = map(int, input().split()) #입력
rest = []

while 1:
    quotient = N_10 // B_2_36 #몫
    rest.append(N_10 % B_2_36) #나머지
    N_10 = quotient
    if quotient == 0:
        break

rest.reverse() #순서 바꾸기
for i in range(len(rest)):
    print(rest[i], end = "")