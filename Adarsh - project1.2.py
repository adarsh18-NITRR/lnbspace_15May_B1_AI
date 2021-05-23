#project   1.2
d = {i:i*i for i in range(1,21)}
s = input('enter a string: ')
a = {i:s.count(i) for i in s}
# print(a)
# print(a.values())
value_list = [j for j in a.values()]
d2 = {x:value_list.count(x) for x in value_list}
# print(d2)


# dict_values([3, 3, 3, 3, 4, 4])
# {3: 4, 4: 2}
if len(d2) == 1:
    print('my string')
elif len(d2) == 2:
    list3 = [y for y in d2.keys()]
    list3.sort()
    f = int(list3[1])
    g = int(list3[0])
    if (f - g) == 1:
        print('my string')
elif len(d2) > 2:
    list4 = [z for z in d2.keys()]
    list4.sort()
    for l in list4[:-2]:
        if l < list4[-2]:
            password = False       # if -2 is not equale to everyone t
        else:
            password = True
    if (int(list4[-1]) - int(list4[-2]) == 1) and password:
        print('this is my string')
    else:
        None
    
    




















