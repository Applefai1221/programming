a = int(input())
b = int(input())
c = int(input())

n = a*b*c
list1 = list(str(n))

for i in range(10):
    print(list1.count(str(i)))