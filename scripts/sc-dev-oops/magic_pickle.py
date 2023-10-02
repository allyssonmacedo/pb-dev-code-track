
# é perigoso, cuidado ao pegar arquivos da internet

import pickle

class A:
    def __init__(self) -> None:
        self.attribute_1 = 1
        self.attribute_2 = 2

    def __str__(self) -> str:
        return f'A({self.attribute_1}, {self.attribute_2})'

    def __getstate__(self):
        self.attribute_1 *= 2
        self.attribute_2 *= 3
        return self.__dict__

    def __setstate__(self, d):
        print('carregando objeto...')
        self.__dict__ = d
    
a = A()
print(a)

with open('a_object.pickle', 'wb') as f:
    pickle.dump(a, f)

with open('a_object.pickle', 'rb') as f:
    a_2 = pickle.load(f)

print(a)
print(a_2)

# import pickle 

# class A: 
#     def __init__(self) -> None: 
#         self.attribute_1 = 1 
#         self.attribute_2 = 2 
        
#     def __str__(self) -> str: 
#         return f"A({self.attribute_1}, {self.attribute_2})"
    
#     def __getstate__(self): 
#         print("Salvando objeto...") 
#         self.attribute_1 *= 2 
#         self.attribute_2 *= 3 
#         return self.__dict__ 
    
#     def __setstate__(self, d): 
#         print("Carregando objeto...") 
#         self.__dict__ = d 

# a = A() 
# print(a) 

# with open("a_object.pickle", "wb") as f: 
#     pickle.dump(a, f) 
    
# with open("a_object.pickle", "rb") as f: 
#     a_2 = pickle.load(f) 
    
# print(a_2) 
# print(a)
