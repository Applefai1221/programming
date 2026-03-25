import math
def prime_number(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

a,b = map(str,input().split())

if prime_number(int(a)) == True and prime_number(int(b + a)) == True:
    print('Yes')
else:
    print('No')  