a, b, c, d = map(int, input().split())

s = a*b*c*d/8/1024/1024

print(f"{s:.1f} MB")
