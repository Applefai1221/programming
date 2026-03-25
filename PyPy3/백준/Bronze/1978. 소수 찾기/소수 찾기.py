import math
def prime_number(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
num = map(int,input().split())
list1 = []

for i in num:
    if prime_number(i):
        list1.append(i)
print(len(list1))