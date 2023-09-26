from copy import copy, deepcopy
a = [1,2,3,[5,6,7]]
b, c = a.copy() , deepcopy(a)
a[0] = 10 ## nao muda nos demais
a[3].append(8) ## muda apenas no shallow copy
print(b,c)


## agora com classes:
class A:
    def __init__(self) -> None:
        self.attr1 = 0
        self.attr2 = [1,2,3]

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
    

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            print(memo)
            print(k, v)
            setattr(result, k, deepcopy(v, memo))
        return result



# a1 = A()
# a2 = copy(a1) 
# a1.attr1 = 10
# a1.attr2.append(4)
# print(a1.__dict__)
# print(a2.__dict__)

print('------')


a1 = A()
a2 = copy(a1) 
a3 = deepcopy(a1)
a1.attr1 = 10
a1.attr2.append(4)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)