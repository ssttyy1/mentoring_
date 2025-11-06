My_total_money = 1000 #보유 금액
Have_to_money = int(input()) # 물건 가격
Change = My_total_money - Have_to_money # 잔돈
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0 # 변수 초기화

if Change >= 500:
    a = int(Change / 500)
    Change = int(Change % 500)
if Change >= 100:
    b = int(Change / 100)
    Change = int(Change % 100)
if Change >= 50:
    c = int(Change / 50)
    Change = int(Change % 50)
if Change >= 10:
    d = int(Change / 10)
    Change = int(Change % 10)
if Change >= 5:
    e = int(Change / 5)
    Change = int(Change % 5)
if Change >= 1:
    f = int(Change / 1)
    Change = int(Change % 1)

print(a + b + c + d + e + f)