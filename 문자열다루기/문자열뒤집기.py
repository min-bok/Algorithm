str = "Hello World"
arr = ["a", "b", "c", "d", "e"]

# 1. reverse() 함수
# arr.reverse()
# print(arr) # ['e', 'd', 'c', 'b', 'a']

# 2. 슬라이싱
# print(arr[::-1]) # ['e', 'd', 'c', 'b', 'a']
# print(str[::-1]) # dlroW olleH

# 3. 투 포인터
def reverseString(s):
    left_idx, right_index = 0, len(s)-1
    while left_idx < right_index:
        s[left_idx], s[right_index] = s[right_index], str[left_idx]
        left_idx += 1
        right_index -= 1
    print(s[left_idx], s[right_index])

# reverseString(arr) # ['e', 'd', 'c', 'e', 'H']
# reverseString(str) # 문자열의 경우 list로 변경후 문자열을 뒤집고 다시 문자열로 변경해주는 과정이 필요함 print("".join(list(str)))