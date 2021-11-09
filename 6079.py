n = int(input())
s = 0

for i in range(1, n):
    s += i
    if s >= n:
        print(i)
        break
