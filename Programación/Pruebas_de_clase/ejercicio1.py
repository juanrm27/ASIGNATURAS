v1 = ['4,8,14,27']
v2 = ['5,11,14,2']
total = 0

for i in range(len(v1)):
    total += v1[i] * v2[i]
print(total)