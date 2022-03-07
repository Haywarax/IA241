#lecture 6


for letter in ['a', 'b', 'c']:
    print(letter)
    
demo_str = 'this is my string'

for c in demo_str:
    print(c)
    
for word in demo_str.split():
    print(word)
    
for i in range(5):
    print(i)
    
print('****************')    
    
for i in range(1,5):
    print(i)
    
print('****************')
    
for i in range(1,5,2):
    print(i)

print('****************')
    
num_list = [213, 321, 123, 312]

max_item = num_list[0]

for num in num_list:
    if max_item <= num:
        max_item = num

print(max_item)
    
num_list2 = [1,12,3,1]

max_item2 = num_list2[0]
for num in num_list2:
    if max_item2 <= num:
        max_item2 = num
        
print(max_item2)

print('****Line49****')

for c in num_list2:
    print(c)
    
print('***Line54****')    
    
for word in num_list2:
    print(word)
    
print('****Line59****')