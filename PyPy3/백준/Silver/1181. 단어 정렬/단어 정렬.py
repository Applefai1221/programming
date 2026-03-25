n = int(input())

list1 = [input() for i in range(n)]

list1 = list(set(list1))
list1.sort()
list1.sort(key = len)

for i in list1:
    print(i)