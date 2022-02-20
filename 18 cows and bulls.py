import random

num_r = []
for number in range(4):
    num_r.append(random.randint(0,9))

attempt = 0
win = False

while win != True:
    
    cow_counter = 0
    bull_counter = 0
    
    num_p_in = input('gimme 4 digit number')
    num_p = [int(num) for num in num_p_in ]
    num_r_c = num_r.copy()
    
    for number in range(4):       
        if num_p[number] == num_r[number]:
            cow_counter +=1 
            num_r_c[number] = None            
    
    for number in range(4):        
        if num_p[number] in num_r_c and num_r_c[number] != None:
            bull_counter +=1
    
    if cow_counter == 4:
        win = True
        attempt += 1
        print(f'you won! number of attempts = {attempt}')
        break
        
    attempt += 1  
    print(f'cows = {cow_counter}, bulls = {bull_counter}')
    print(f'number of attempts: {attempt}')
    
 
    
