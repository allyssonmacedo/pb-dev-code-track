class A: 
    def __new__(cls, *args, **kwargs): 
        print("new", cls, args, kwargs) 
        return super().__new__(cls) 
    
    def __init__(self, *args, **kwargs) -> None: 
        print("init", self, args, kwargs) 
        
class Meters(float): 
    def __new__(cls, kilometers): 
        meters = kilometers * 1000 
        return super().__new__(cls, meters)
    

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
A = Singleton()
B = Singleton()
