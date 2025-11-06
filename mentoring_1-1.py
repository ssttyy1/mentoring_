def how_many_basket():
    print("상자를 1부터 100까지 원하는 수 까지 차례대로 쓰시오.")
    basket = list(map(int, input().split()))#입력 받은걸 어떻게 변환하는지 모르겠어서 참고했음
    return basket

def exchange_ball(basket):
    print("몇 번 교환 하실건가요?")
    exchange = int(input())
    for i in range(exchange):
        print("서로 교환할 상자 2개를 선택하시오.")
        ball1 = int(input())
        ball2 = int(input())
        basket[ball1-1], basket[ball2-1] = basket[ball2-1], basket[ball1-1]
    return basket


basket = how_many_basket()
result = exchange_ball(basket)

print("교환 된 상자 상태", result)