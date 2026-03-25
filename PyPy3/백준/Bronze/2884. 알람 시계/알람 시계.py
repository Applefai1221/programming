h,m = map(int,input().split())

if m >= 45:
    print(h,end=' ')
    print(m - 45)
elif m < 45 and h >= 1:
    print(h - 1,end =' ')
    print(m + 15)
elif m < 45 and h < 1:
    print(23,end = ' ')
    print(m + 15)