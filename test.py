data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

goal = [
    [5, 1],
    [6, 2],
    [7, 3],
    [8, 4]
]

data = list(zip(*data[::-1]))

for i in data:
    print(i)