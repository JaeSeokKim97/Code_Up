a, b, c = map(int, input().split())
count = 0
for i in range(0, a):
    for k in range(0, b):
        for j in range(0, c):
            count += 1
            print(i, k, j)

print(count)