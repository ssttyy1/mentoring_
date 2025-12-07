a = input()
b = input()
c = input()

line = [a, b, c]
num = 0 #숫자 받아오기
ott = 0 #몇 번째 수 인지 확인

for i in range(3):
    if line[i].isdigit():
        num = int(line[i])
        ott = i
        break

start_num = num - ott

next_num = start_num + 3

if next_num % 15 ==0:
    print("FizzBuzz")

elif next_num % 5 == 0:
    print("Buzz")

elif next_num % 3 == 0:
    print("Fizz")

else:
    print(next_num)