#  list
list = ["one", "two","three", "four", "five" ]
list.append("six") # ['one', 'two', 'three', 'four, 'five', 'six']
list.pop() # ['one', 'two', 'three', 'four', 'five']
list.pop(1) # ['one', 'three', 'four', 'five']
del(list[1]) # ['one', 'four', 'five']
list.index("five") # 2
list.insert(1, "new") # ['one', 'new', 'four', 'five']

print(list)