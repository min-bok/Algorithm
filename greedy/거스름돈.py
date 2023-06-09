"""
500원, 100원, 50원, 10원짜리 동전이 있을때, 손님에게 N원을 거슬러주기위한
동전의 최소 개수를 구하세요. 단 거슬러줘야 할 돈 N은 항상 10의 배수입니다.
"""
# 시간 복잡도 분석
"""
- 화폐의 종류가 k라고 할때, 소스코드의 시간복잡도는 O(k)
- 이 알고리즘의 시간복잡도는 거슬러줘야하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받음
"""
n = 1260

def change(n):
    cnt  = 0
    money = [500, 100, 50, 10]

    for coin in money:
        cnt += n // coin
        n %= coin 

    return cnt

print(change(n))
