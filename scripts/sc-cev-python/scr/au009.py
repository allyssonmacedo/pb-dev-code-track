#Manipulando Texto
frase = 'Curso em Video Python'
print(frase)
print(frase[9])
print(frase[9:21:2]) #começa do 9 e vai ao 21 e pula 2 em 2
print(frase[:5]) #inicio ao 5
print(frase[15:]) #15 ao final
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))  #Se aparecer -1 é pq não existe
print('Curso' in frase)
frase.replace('Python','Android')
frase.upper() #muda tudo p maiúscula
frase.lower() #minusculo
frase.capitalize() 
frase.title()
frase.strip() #remove espaços inúteis no ínicio e fim
frase.rstrip() # remove só os da direita
print(frase.split()) #quebra as palavras 
frase2 = frase.split()
print('-'.join(frase2)) #junta as palavras quebradas pelo slipt e coloca um '-' entre elas
print("""aqui vem um texto grandeeeeeeeeeeeeeeeeeeeeeeeeee
      eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee""")

print(len(frase.strip()))
frase = frase.replace('Python', 'Android')
print(frase)
dividido = frase.split() 
print(dividido[2][3]) 


#listahash = [0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f]