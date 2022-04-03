class car:
    
    maker = 'toyota'
    
    def __init__(self,input_model):
        
        self.model = input_model
        
    def report(self):    
        
        return self.maker, self.model
        

my_corolla = car('corolla')      

my_highlander = car('highlander')

print(my_corolla.maker, my_corolla.model)

print(my_highlander.maker, my_highlander.model)

my_corolla.maker = 'ford'

print(my_corolla.maker)

print(my_corolla.report())

