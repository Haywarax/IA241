#Lecture 7


i = 5 

while i >=0:
    
    i = i - 1
    
    if i == 3:
        continue
    
    print(i)
    
try:
    print(1/0)
    
except:
   print('')
   
print('*****************')

i = 5 

while i >=0:

    try:
        print(1/(i-3))
    
    except:
        continue
    
    i = i - 1
    
    print(i)
    

    
