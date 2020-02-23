def h(x):
    black = 0
    for i in range(len(x)):
        if x[i] == "1":
            black += 1
    return black
