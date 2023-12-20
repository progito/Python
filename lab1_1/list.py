list = list()
for value in range(0,7):
    value = int(input("введите список"))
    list.append(value)
n = len(list)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if list[j] > list[j + 1]:
            # swap elements
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)
