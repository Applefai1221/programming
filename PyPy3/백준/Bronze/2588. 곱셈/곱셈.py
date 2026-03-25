number1 = input()
number2 = input()

first_list = list(map(int,str(number1)))
a = first_list[0]
b = first_list[1]
c = first_list[2]
second_list = list(map(int,str(number2)))
d = second_list[0]
e = second_list[1]
f = second_list[2]

g = 10
h = 100
i = 1000
j = 10000

print(c*f + b*f*g + a*f*h)
print(c*e + b*e*g + a*e*h)
print(c*d + b*d*g + a*d*h)
print(c*f + b*f*g + a*f*h + c*e*g + b*e*h + a*e*i + c*d*h + b*d*i + a*d*j)