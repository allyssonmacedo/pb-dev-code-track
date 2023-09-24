class Celsius: 
    def __get__(self, instance, owner): 
        if instance.unit == "Fahrenheit": 
            return (instance.value - 32) / 1.8 
        
        elif instance.unit == "Kelvin": 
            return (instance.value - 273.15) 
        
        elif instance.unit == "Celsius": 
            return instance.value 
        
        else: 
            raise Exception("Unidade de Temperatura Inválida..") 
        
    def __set__(self, instance, value): 
        pass 
    
    def __delete__(self, instance): 
        pass 
    
class Machine: 
    temp = Celsius() 
    def __init__(self, temp_value, temp_unit="Celsius") -> None: 
        self.value = temp_value 
        self.unit = temp_unit 
        
machine = Machine(100, temp_unit="Kelvin") 
print(machine.temp)
