list1 = []
while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    s = a + b
    list1.append(s)

for i in range(int(len(list1))):
     print(list1[i])