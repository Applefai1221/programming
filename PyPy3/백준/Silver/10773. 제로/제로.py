n = int(input())
list1 = []

for i in range(n):
    num = int(input())
    if num == 0:
        list1.pop()
    else:
        list1.append(num)
print(sum(list1))