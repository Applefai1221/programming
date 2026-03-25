list1 = []

for i in range(int(input())):
    a,b = map(int,input().split())
    list1.append((a,b))

list1.sort(key = lambda x : (x[0], x[1]))

for i in list1:
    print(i[0], i[1])