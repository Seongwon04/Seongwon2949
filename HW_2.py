def sum_num(N_list):
    if len(N_list) < 1:
        return 0
    else:
        return int(N_list[0]) + sum_num(N_list[1:])
    
    


while True:
    num = input('Enter integers separated by spaces ==> ')
    if num == 'done':
        print('program terminated. good bye !!')
        break
    num_list = num.split()
    int_num = True
    for test in num_list:
        try:
            int(test)
        except ValueError:
            print('must enter integers separated by spaces')
            int_num = False
            break
    if len(num_list) == 1:
        print('must enter more than one integer')
        continue
    if int_num:
        print('The sum of the input integers is',sum_num(num_list))
        break
    
    
        
    

        
 
    