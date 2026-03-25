n = int(input())
if n == 0:
    print(0)
    exit()

list1 = []
for i in range(n):
    list1.append(int(input()))
list1.sort()

s = int(n * 0.15 + 0.5)

t = 0
for i in range(s, n - s):
    t += list1[i]
n3 = int(t/(n - 2*s) + 0.5)
print(n3)