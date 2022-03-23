# Lecture 8

def my_function (a,b):
    
    result = a + b
    
    print(a)
    
    print(b)
    
    return(result)
    
print(my_function(b=1, a=2))    

print('****************')

def cal_abs(a):
    
    if a>0:
        return 0
        
    if a<0:
        return -a
        
print(cal_abs(-1))  

print('***************')

def cal_abs(a):
    
    if type(a) is str:
        return 'wrong data type'
        
    elif a >-0:
        return a
        
    else:
        return -a
    
print('************')

def cal_sigma(n,m):

    result = 0

    for i in range(n,m+1):

        result = result + i
    
        result - 1
    
    return(result)
    
print(cal_sigma(1,5))

print('*************')

def cal_pi(n,m):
  
    result = 1
    
    for i in range(n,m+1):
    
        result = result * i
    
    return result
    
print(cal_pi(5,3))
    

    