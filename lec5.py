#*******

#Lecture 5: If Statements


#*******

#import this

print( 1+
        1)
        
print([1,2,3,
        4,5,6])  
        
m = 1 +\
        2
        
print(m)

a= [1,2,3]
b= [1,2,3]

print(id([1,2,3]))
print(id(a))
print(id(b))

print(a == b)
print(a is b)

x = None

print(id(x))
print(id(None))

print(x is None)
print(x == None)

y = []

print(y == None)
print(y is None)

print( True and False)
print( True or False)
print(not True)
print(not False)

print('********************')

print(not '0')
print(not 0)
print(not None)

print(() and [])
# equivalent of print(false and false)

print([] and ())

print(-1 or 0)

print('************************')

if 2>1 : 
        print('2>1')

        if 3>1 : 
                print('3>1')

        if 2<1 : 
                print('2<1')
                
if 2<=2:
        print("2<=1")
        
else: print('2>2')

print("***************")

if 2<1:
        print('2<1')
elif 2<=2:
        print('2<=2')
else:
        print('2>1')