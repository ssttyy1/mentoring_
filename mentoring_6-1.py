i = input()
result = ""
count = 0 #X개수 세기

for j in i: # 변수 i에서 문자를 1개씩 받아옴
    if j == "X":
        count += 1
    else: #X이외의 문자를 만났을 때
        if count % 2 == 1:
            print(-1)
            exit()

        result += "A" * (count // 4 * 4)
        result += "B" * (count % 4)
        result += "."
        count = 0

if count % 2 == 1: #마지막 부분이 X면 뒤에 입력이 없어서 마지막 부분이 생략됨
    print(-1)
else:
    result += "A" * (count // 4 * 4)
    result += "B" * (count % 4)
    print(result)