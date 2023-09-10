## Crie um programa que tenha uma função chamada votar () que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicado se uma pessoa tem voto negado, opcional, ou obrigatório nas eleições.
#from datetime import datetime

def votar(year_birth):
    """
    Retorna voto negado, opcional ou obrigatório depenendo da idade da pessoa
    args:
        year_birth -> ano de nascimento da pessoa  
    exemplo:
        votar(1998) -> 'obrigatório'
    """
    from datetime import datetime
    
    current_year = datetime.now().year
    age = current_year - year_birth

    if age >= 18 and age <= 65:
        return f"Com {age} anos o voto é Obrigatório"
    elif age <16:
        return f"Com {age} anos o voto é Negado"
    else:
        return f"Com {age} anos o voto é Opcional"
    
print(votar(1998))

