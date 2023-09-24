class Numeric: 
    def __init__(self, dependent_number, independent_number) -> None: 
        self.dependent = dependent_number 
        self.independent = independent_number # a * x + b 
        
    def solve_problem(self, x_value): 
        return (self.dependent * x_value) + self.independent 
        
    def __add__(self, __other): 
        result_dependent = self.dependent + __other.dependent 
        result_independent = self.independent + __other.independent 
        return Numeric(result_dependent, result_independent) 
        
    def __sub__(self, __other): 
        result_dependent = self.dependent - __other.dependent 
        result_independent = self.independent - __other.independent 
        return Numeric(result_dependent, result_independent) 
    
    def __mul__(self, __other): 
        result_dependent = self.dependent * __other.dependent
        
        result_independent = self.independent * __other.independent 
        return Numeric(result_dependent, result_independent) 
    
    def __repr__(self) -> str: 
        return f"Numeric({self.dependent}, {self.independent})" 
    
    def __str__(self) -> str: 
        return f"{self.dependent} * x + {self.independent}" 
    
num_1 = Numeric(1, 2) 
num_2 = Numeric(4, 5) 
print(num_1 + num_2) 
print(num_1 - num_2) 
print(num_2 - num_1) 
print(num_2 * num_1)

#https://docs.python.org/3/reference/datamodel.html
#emulating-numeric-types