n = input()
list1 = []

for i in range(int(n)):
    list1.append(input())

for j in range(int(n)):
    if 6 <= len(list1[j]) <= 9:
        print("yes")
    else:
        print("no")