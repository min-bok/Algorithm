def solution(L, x):
    answer = -1
    lower = 0
    upper = len(L) - 1
    
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            answer = middle
            break
        elif L[middle] < x:
            lower = middle
        else:
            upper = middle
        break
    return answer