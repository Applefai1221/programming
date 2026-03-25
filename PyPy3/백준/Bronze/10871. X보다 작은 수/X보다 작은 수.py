n,x = map(int,input().split())
list1 = list(map(int, input().split()))
list2 = []

for i in range(n):
    if list1[i] < x:
        list2.append(list1[i])

for i in range(len(list2)):
    print(list2[i], end = ' ')