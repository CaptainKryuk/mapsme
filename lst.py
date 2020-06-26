# lst = [5,1,5,8,2,5]
lst = list(range(10*10))

for i in range(len(lst)):
    lst[i] = lst[len(lst) -1] - i