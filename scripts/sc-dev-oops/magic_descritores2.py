class Number:     
    def __set_name__(self, owner, value):
        self.name = value     
        
    def __get__(self, instance, owner):         
        return instance.__dict__.get(self.name, None)     
    
    def __set__(self, instance, value):         
        instance.__dict__[self.name] = (value if value % 2 == 0 else 0) 
        

class Values:     
    value1 = Number()    
    value2 = Number()     
    value3 = Number()     
    value4 = Number()     
    value5 = Number() 

my_values = Values() 
my_values.value1 = 1 
my_values.value2 = 4 
print(my_values.value1) 
print(my_values.value2)


### Logica que retira getter e setter para cada uma dos values