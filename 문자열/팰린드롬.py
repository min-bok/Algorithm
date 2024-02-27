def ispalindrome(str):
    for i in range(len(str)//2):
        if str[i] == str [-i-1]:
            continue
        else:
            print("팰린드롬이 아닙니다.")
    print("팰린드롬 입니다.")

data = "abcba"

ispalindrome(data)