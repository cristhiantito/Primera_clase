import random

def generar_contraseña(valor):
    mayusculas = ['A','B','C','D','E','F','G','H']
    minusculas = ['a','b','c','d','e','f','g','h']
    simbolos =['!','#','$','%','&',]
    numeros = ['1','2','3','4','5','6','7','8','9']
    caracteres = mayusculas + minusculas + simbolos + numeros
    contraseña = []
    for i in range(valor):
        caracter_random = random.choice(caracteres)
        contraseña.append(caracter_random)
    
    contraseña = "".join(contraseña)
    return contraseña
valor = float(input(f'Ingrese la catidad que qiere su contraseña:  '))
nueva_contraseña = generar_contraseña(valor)
print(f'Tu nueva contraseña es: {nueva_contraseña}')
