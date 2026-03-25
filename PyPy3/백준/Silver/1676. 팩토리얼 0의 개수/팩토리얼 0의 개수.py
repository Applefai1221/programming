n = int(input())
t = 1
f = 0

for i in range(1, n + 1):
    t = t * i
    
list1 = list(str(t))
list1.reverse()

while True:
    if list1[f] == str(0):
        f += 1
    else:
        print(f)   
        break
    