n = 9

number = []
for i in range(n):
    number.append(int(input()))

t = 0 
for j in range(n):
    if t < number[j]:
        t = number[j]

print(f'''{t}
{number.index(t) + 1}''')