# 팰린드롬(회문)이란 앞뒤가 똑같은 단어나 문장을 의미함
# 대소문자를 구분하지않으며 문자와 숫자만 따지면됨
# 만약 팰린드롬에 대소문자나 특수기호 포함시 이를 제거하는 전처리작업 후 판별을 시행

def ispalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str [-i-1]:
            continue
        else:
            print("팰린드롬이 아닙니다.")
    print("팰린드롬 입니다.")

data = "abcba"

ispalindrome(data)