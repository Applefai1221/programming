list1 = []
for i in range(28):
    list1.append(str(input()))
for i in range(1,31):
    if list1.count(str(i)) == 0:
        print(i)