m = input()
n = int(m, 16)
for k in range(1, 16):
    print('%X'%n, '*%X'%k, '=%X'%(n*k), sep='')