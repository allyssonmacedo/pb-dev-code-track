class Baggage: 
    def __init__(self, items: list) -> None: 
        self.items = items 
        
    @property 
    def items(self): 
        return self._items 
    
    @items.setter 
    def items(self, value): 
        if isinstance(value, list): 
            self._items = value 
        else: 
            raise Exception("Valor Inválido...") 
    
    def __getattr__(self, attr_name): 
        print("__getattr__") 
        return self.__dict__.get(attr_name, None) 

    def __setattr__(self, __name, __value) -> None: 
        print("__setattr__") 
        self.__dict__[__name] = __value 
        return __value 
    
    def __delattr__(self, __name) -> None: 
        value = self.__dict__.get(__name, None)
        self.__dict__.__delitem__(__name) 
        print(f"Atributo {__name} deletado com valor {value}") 
        
bag = Baggage(["Item 1", "Item 2"]) 
print(bag.name) 
print(bag.items) 
bag.name = "Iury Rosal" 
bag.items = ["Item 1", "Item 2", "Item 3"] 
print(bag.__dict__) 
del bag.name 
del bag.color ## é para dar erro 