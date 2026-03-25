list1 = []
list2 = []
for i in range(10):
    list1.append(int(input()))
for i in range(10):
    s = list1[i] % 42
    list2.append(s)
n = set(list2)
print(len(n))