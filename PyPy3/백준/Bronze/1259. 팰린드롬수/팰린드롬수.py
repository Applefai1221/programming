while True:
    a = input()
    if a == '0':
        break
    list1 = list(a)
    list2 = list1[::-1]
    if list1 == list2:
        print('yes')
    else:
        print('no')