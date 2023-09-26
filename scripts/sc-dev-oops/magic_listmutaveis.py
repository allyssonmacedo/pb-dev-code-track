class SpecialList: 
    def __init__(self, list_of_elements: list) -> None: 
        i = 0 
        self.data = {} 
        for elem in list_of_elements: 
            self.data[str(i)] = elem 
            i += 1 
            
        self.size = i 
        
    def __len__(self) -> int: 
        return self.size 
    
    def __getitem__(self, index): 
        return self.data.get(str(index), None) 
    
    def __setitem__(self, index, new_value):
        if self.data.get(str(index), False):
            self.data[str(index)] = new_value

        else:
            raise IndexError('Index not exists')
        
    def __delitem__(self, index):
        if self.data.get(str(index), False):
            del self.data[str(index)]
            self.size -= 1

        else:
            raise IndexError('Index not exists')
    
    def append(self, value): 
        self.data[str(self.size)] = value 
        self.size += 1 
        return True 
    
    def pop(self): 
        del self.data[str(self.size - 1)] 
        self.size -= 1 
        return True 
    
special_list = SpecialList([1, 2, 3, 4, 5]) 
print(special_list.__dict__) 
special_list.append(6) 
print(special_list.__dict__) 
special_list.pop()
print(special_list.__dict__) 
print(special_list[4]) 
special_list[4] = 10