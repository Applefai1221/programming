n = int(input())
list1 = list(map(int,input().split()))

max = max(list1)

t = 0
for i in list1:
    t += i / max * 100

print(t / n)