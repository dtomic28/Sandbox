dat1 = open("ref.txt", "r")
dat1R = dat1.read()
dat2 = open("sif.txt", "r")
dat2R = dat2.read()

slovar1 = {}
slovar2 = {}

for i in dat1R:
    if i not in slovar1:
        slovar1[i] = 1
    else:
        slovar1[i] += 1

for i in dat2R:
    if i not in slovar2:
        slovar2[i] = 1
    else:
        slovar2[i] += 1

print(slovar1)
print("\n")
print(slovar2)

res = ' '.join(sorted(slovar1, key = lambda key: slovar1[key]))

print(res)
