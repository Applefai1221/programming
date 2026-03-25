n = int(input())
list1 = []

for i in range(n):
    x,y = input().split()
    list1.append([int(x),y])
list1.sort(key = lambda x : x[0])

for i in list1:
    print(i[0], i[1])