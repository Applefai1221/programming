n,a,b = map(int,input().split())

if a < b:
    print("Bus")
elif a > b and b >= n:
    print("Subway")
elif a > b and b < n:
    print("Bus")
elif a == b and b >= n:
    print("Anything")