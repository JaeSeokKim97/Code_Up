a, b, c = map(int, input().split())

s = a*b*c/8/1024/1024

print(f"{s:.2f} MB")
