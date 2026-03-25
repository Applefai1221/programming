import math
def prime_number(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

a,b = map(int,input().split())

for i in range(a,b + 1):
    if prime_number(i):
        print(i)