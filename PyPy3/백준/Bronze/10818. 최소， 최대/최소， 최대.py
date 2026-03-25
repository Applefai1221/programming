n = int(input())

list1 = list(map(int, input().split()))
t = -1000001
for i in range(n):
    if t < list1[i]:
        t = list1[i]

f = 1000001
for j in range(n):
    if f > list1[j]:
        f = list1[j]

print(f, t)