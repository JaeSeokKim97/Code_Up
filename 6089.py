a, b, c = map(int, input().split())
cut = 0
while(1):
    a *= b
    cut += 1
    if cut == c-1:
        print(a)
        break
