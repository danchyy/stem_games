import numpy as np

def has_roots(num):
    if (num==1) :
        return True 
    for x in range(2,int(np.sqrt(num))+1):
        y = 2
        p = np.power(x, y)
        while (p>0 and p<=num):
            if (p==num):
                return True           
            y += 1
            p = np.power(x, y) 
    return False

def find_nums(L,U):
    nums = []    
    for i in range(L,U):
        if (has_roots(i)):
            nums.append(i)   
    return(nums) 

def get_solution(string):
    L = int(string.split(" ")[0])
    U = int(string.split(" ")[1])
    return len(find_nums(L,U))
    
    



