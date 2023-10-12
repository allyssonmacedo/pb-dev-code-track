def exibir_resultado(n=None):

    def decorador(func):

        print('decorador aqui')

        def closure(*args, **kwargs):
            print(n)
            result = func(*args, **kwargs)
            print(f'O resultado da função {func.__name__} é {result}')
            
            return None
    
        return closure
    return decorador

@exibir_resultado()
def sum(x,y):
    return x+y


sum(1,1)
