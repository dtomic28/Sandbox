
def rekuzija(x):
    if x == 1:
        return 1
    else:
        return x * rekuzija(x-1)


print(rekuzija(6))