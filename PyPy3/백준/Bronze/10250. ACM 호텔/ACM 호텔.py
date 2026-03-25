t = int(input())
list1 = []

for i in range(t):
    h,w,n = map(int,input().split())
    for j in range(1,w + 1):
        for k in range(1,h + 1):
            if 1 <= j < 10:
                list1.append(int(str(k) + str(0) + str(j)))
            elif 10 <= j:
                list1.append(int(str(k) + str(j)))
    print(list1[n-1])
    list1.clear()