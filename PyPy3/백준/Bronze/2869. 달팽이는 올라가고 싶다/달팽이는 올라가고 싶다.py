a,b,v = map(int,input().split())
n1 = v - a
n2 = a - b
if n1 % n2 == 0:
    print(int(n1/n2) + 1)
else:
    print(int(n1/n2) + 2)