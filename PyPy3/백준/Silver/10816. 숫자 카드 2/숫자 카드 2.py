from collections import Counter

n = int(input())
list1 = list(map(int,input().split()))
m = int(input())
list2 = list(map(int,input().split()))

s = Counter(list1)
for i in list2:
    print(s[i],end = ' ')