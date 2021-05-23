import time

register = input('do you want to register? (y/n)')
if register.upper() == 'Y':   
    name_user = input('Enter Username: ')
    password = True
    #while loop for checking password and promptning to enter until enter correct password
    while password:  
        pass_user = input('Input Password: ')
        if len(pass_user)>8:
            print(f'{pass_user} is too long to be password')
            continue
        for i in pass_user:
            random_num = 0
            if i.isdigit()==False:
                random_num = 1
                continue
            elif i.isdigit()==True:
                break
        # next set of  conditions        
        if random_num == 1:
            print('you dont have a digit')
        elif pass_user.upper() == pass_user:
            print('you dont have a small character! ')
        elif pass_user.lower() == pass_user:
            print('you dont have a capital character! ')
        else:
            break
    print('you have successful registered.....Loading......')
    time.sleep(7)
    
    #checking password
    
    test_user = input('enter your username')
    test_pass = input('enter your password')
    
    
    if (name_user == test_user) and (test_pass == pass_user):
        print('loading.......')
        time.sleep(6)
        
        #asking user for things
    
        welcome = input('Hello user. What you want?\n1)Calculator(C)\n2)Table Genarator(T)\n3)Pattern Geerator(P)')
        if welcome.upper() == 'C':
            operation = input('what you want to do? Multiple(m), Add(a), Divide(d), Subtract(s):\n')
            f_num, s_num = int(input('Enter first number: ')),int(input('Enter Second number: '))
            try: 
                if operation.upper() == 'M':
                    print(f_num*s_num)
                    print('thanks for using this!')
                elif operation.upper() == 'A':
                    print(f_num + s_num)
                    print('thanks for using this!')
                elif operation.upper() == 'S':
                    print(f_num - s_num)
                    print('thanks for using this!')
                elif operation.upper() == 'D':
                    print(f_num / s_num)
                    print('thanks for using this!')
                else:
                    print('wrong value , program terminates! ')
                    
            except ValueError:
                print('enter a number')        
            
        elif welcome.upper() == 'T':
           whose_table = int(input('Enter Number! '))
           for i in range(1,11):
               print(whose_table*i)
           print('thanks for using this!')    
        elif welcome.upper() == 'P':
            how_long_pattern = int(input('How long pattern? '))
            for i in range(1,how_long_pattern+1):
                s = ""
                for j in range(1,i+1):
                    s += str(j) + " "
                print(s.strip())    
            print('thanks for using this!')   
    else:
        print('program terminates in 10 secs due to incorrect password/ username!')
        time.sleep(10)
        exit()
        
elif register.upper() == 'N':
    print('program ends in 10 seconds')
    time.sleep(10)
    exit()
    

