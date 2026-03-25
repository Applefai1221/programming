a,b,c,d,e = map(int, input().split())
f = 2
plus = pow(a,f) + pow(b,f) + pow(c,f) + pow(d,f) + pow(e,f)
print(plus % 10)