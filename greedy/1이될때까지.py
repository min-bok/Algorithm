"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려합니다.
단 두 번째 연산은 N이 K로 나누어떨어질때만 선택할 수 있습니다.
1. N에서 1을 뺍니다.
2. N을 K로 나눕니다.

입력예시 25 5
출력예시 2

입력예시 25 3
출력예시 6
"""

input = "25 5"
input2 = "25 3"

# def div(input):
#     cnt = 0
#     n, k = map(int, input.split())

#     while not n == 1:
#         if n % k == 0:
#             n //= k
#             cnt += 1
#         else:
#             n -= 1
#             cnt += 1

#     return cnt

# print(div(input))
# print(div(input2))

# 답안예시: 시간복잡도 측면에서 효율, but 아직 이해못함
# def best(input):
#     result = 0
#     n, k = map(int, input.split())

#     while True:
#         # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
#         target = (n // k) * k
#         result += (n - target)
#         n = target
#         # n이 k보다 작을때 (더 이상 나눌 수 없을때) 반복문 탈출
#         if n < k:
#             break
#         # k로 나누기
#         result += 1
#         n //= k
#     # 마지막으로 남은 수에 대하여 1씩 빼기
#     result += (n - 1)
#     print(result)
    

# best(input)
# best(input2)
