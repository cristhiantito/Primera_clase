a = float(input('Ingresa tu primer número: '))
b = float(input('Ingresa tu segundo número: '))
c = float(input('Ingresa tu tercer número: '))
d = float(input('Ingresa tu tercer número: '))
lista = [a,b,c,d]
menor = None
mayor = None
for numero in lista:
    if menor == None and mayor == None:
        menor = numero
        mayor = numero
    else :
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
print(f'El nuemro mayor es, {mayor}')
print(f'Elnumero menor es, {menor}')