class Person:
    def __init__(self, name, age) -> None: 
        self.name = name 
        self.age = age 
        
    def __str__(self) -> str: 
        return f"Pessoa chamada {self.name}, com idade de {self.age}" 
    
    def __repr__(self) -> str: 
        return f"{self.__class__.__name__}({self.name}, {self.age})" 
    
person = Person("Iury", 22) 
print(person) 
print(repr(person)) 
print(person.name)