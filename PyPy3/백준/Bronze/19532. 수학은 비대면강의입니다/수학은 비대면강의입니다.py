a,b,c,d,e,f = map(int,input().split())

for i in range(-999,1000):
    x =i
    for j in range(-999,1000):
        y = j
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)