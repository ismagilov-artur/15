def take_large_banknotes(arr):
    return list(filter(lambda x : x > 10, arr ))
print(*take_large_banknotes([]))
print(*take_large_banknotes([1, 5, 500, 0.5,
2, 0.1, 10, 100, 100, 1000, 50]))