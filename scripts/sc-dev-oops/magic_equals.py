class Word: 
    def __init__(self, word) -> None: 
        self.content = word 
    
    def __eq__(self, __o: object) -> bool: 
        print("Comparando igualdade...") 
        return len(self.content) == len(__o.content) 
    
    def __gt__(self, __o: object) -> bool: 
        print("Comparando >...") 
        return len(self.content) > len(__o.content) 
    
    def __lt__(self, __o: object) -> bool: 
        print("Comparando <...") 
        return len(self.content) < len(__o.content) 
    
    def __le__(self, __o: object) -> bool: 
        print("Comparando <=...") 
        return len(self.content) <= len(__o.content) 
    
    def __ge__(self, __o: object) -> bool: 
        print("Comparando >=...") 
        return len(self.content) >= len(__o.content) 
    
    def __ne__(self, __o: object) -> bool: 
        print("Comparando !=...") 
        return len(self.content) != len(__o.content) 
    
word_1 = Word("Carro") 
word_2 = Word("Bicicleta") 
print(word_1 == word_2) 
print(word_1 != word_2) 
print(word_1 >= word_2) 
print(word_1 <= word_2) 
print(word_1 > word_2) 
print(word_1 < word_2)