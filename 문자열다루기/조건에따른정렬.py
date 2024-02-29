data = ["1 A", '1 B', '6 A', '2 D', '4 B']


def func(x):
    return x.split()[1], x.split()[0] # x.split()[1] 값을 기준으로 오름차순 정렬

data.sort(key=func)
# data.sort(key=func, reverse=True) # 내림차순 정렬

print(data)