# _______________________________________question 1
# list1 = [1,2,3,4,5,6,7,8,9,345,18]
# #final_list = [i for i in list1 if not i%2]
# final_list = []
# for i in list1:
#     if not int(i)%2 and i<=237:
#         final_list.append(i)
#     elif i>237:
#         break
# print(final_list)  
 

# _______________________________________question 2
# color_list_1 = set(["White", "Black", "Red"]) 
# color_list_2 = set(["Red", "Green"])
# print(color_list_1-color_list_2)                                  #subtracting elements of list2 from list1


# _______________________________________question 3
# import string
# input_string = input('enter stirng you want to check')            #taking input
# list_ofalpha = [string.ascii_lowercase]                           #list of all alphabets
# pangram = "is pangram"
# for i in list_ofalpha:                                            #loop for checking existance of all alphabets
#     if i not in input_string:
#         pangram = "not pangram"
# print(pangram)
        

# _______________________________________question 4
# try:
#     ipnum = int(input('input your number'))                       #parsing because want only int as input
#     final_ans = ipnum + (ipnum*10+(ipnum)) + ((ipnum*100)+(ipnum*10+(ipnum)))
#     print(final_ans)   
# except ValueError:
#     print('try entering a integer')


# _______________________________________question 5
# x = input('enter your input').split('#')
# list1 = []
# for i in range(len(x)):                                   #loop for making list of numbers
#     list1.append(x[i].strip().split(' '))
# for i in range(len(list1)):                               #loop for converting string objects to int
#     for j in range(len(list1[i])):
#         if list1[i][j].isdigit() == True :    
#             list1[i][j] = int(list1[i][j])
#         else:
#             list1[i][j] = 'this wasn\'t a number' 
# def list_maker(j):                                        #loop for printing seperate list from final combined list that contained ontegrers
#     for i in j:
#         print(i)
# list_maker(list1)


# _______________________________________question 6
# main_str = input('enter your string: ').rstrip(',').split(',')      #making list; removing extra ',' 
# main_str.sort()                                                     #sorting alphabetically
# s = ''
# for i in main_str:                                                  #adding words to a string
#     s = s + i + ", "
# print(s.rstrip(', '))

# _______________________________________question 7
# d = {'names':['rahul','kishor','vaidhya','rakhi'],
#      'marks' : [23,45,67,54]
#      }
# x = list(zip(d['names'],d['marks']))                                  #combinaing names with marks
# for i in x:
#     if i[1] == max(d['marks']                                         #condition to write name if its marks = maximum marks
#         print(i[0])


#______________________________________question 8
# main_str = input('enter your string')
# num = 0         #variable for number of digits
# alpha = 0       #variable for number of alphabets
# for i in main_str:
#     if i.isalpha():                                                   #adding 1 to number if that paticular character is digit
#         num = num + 1
#     elif i.isdigit():
#         alpha = alpha + 1                                             #adding 1 to number if that paticular character is digit
# print('numbers: ',num)
# print("alphabets: ",alpha)



#______________________________________question 9
# dict1 = {'name' : ['akash', 'soniya', 'vishakha' , 'akshay', 'rahul', 'vikas'],
#           'subjects' : ['python', 'java', 'python', 'c++' , 'python' , 'java'],
#           'rating' : [8.4, 7.8, 8, 9, 8.2, 5.6]}
# lang = input('enter your language: ')
# x = list(zip(dict1['name'],dict1['subjects'],dict1['rating']))          #collecting together the name rating and subbbejct of person together
# new_data = {}
# new_data['name'] = [i[0] for i in x if i[1]==lang.lower()]              #adding name to list of dictionary whose language is same as input language
# new_data['subjects'] = [i[1] for i in x if i[1]==lang.lower()]
# new_data['rating'] = [i[2] for i in x if i[1]==lang.lower()]
# print(new_data)


# 

#______________________________________question 10
# n = int(input())
# divBy7 = [i for i in range(0, n) if (i % 7 == 0)]                     # list comprehension for adding to list if number in that range is divible by 7
# print(divBy7)





#______________________________________question 11
# import math
# direc = input('enter your directions seperated by commas: ').split(',')
# verticle,horizontal = 0 , 0                                              #initial position variables    
# list1 = [i.strip().split(" ") for i in direc]
# for i in list1:
#     if i[0].upper() == 'UP':
#         verticle = verticle + int(i[1])
#     elif i[0].upper() == 'DOWN':
#         verticle = verticle - int(i[1])
#     elif i[0].upper() == 'RIGHT':
#         horizontal = horizontal + int(i[1])
#     elif i[0].upper() == 'LEFT':
#         horiozontal = horizontal - int(i[1])
# print(f"the final position from 0,0 is {verticle}, {horizontal}")
# distance = round(math.sqrt((verticle**2)+(horizontal**2)))
# print(f'the final distance from 0,0 is {distance}')
