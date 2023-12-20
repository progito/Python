
dict = {
    "4": "Alex",
    "2": "Kate",
    "5": "john",
    "2": "Oleg",
    "1": "Olga",
    "432": "Vadim",
    "-43": "Fedor"
    }
keys = list(dict.items())
n = len(keys)
print(keys)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if int(keys[j][0]) < int(keys[min_index][0]):
            min_index = j
    keys[i], keys[min_index] = keys[min_index], keys[i]
print(keys)
