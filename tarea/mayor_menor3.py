a = float(input('Ingresa tu primer número: '))
b = float(input('Ingresa tu segundo número: '))
c = float(input('Ingresa tu tercer número: '))
if  a == b or a == c or c == b :
    print ('error')
else:
    if a < b and a < c :
        menor = a
        if b < c:
            medio = b
            mayor = c
        else :
            medio = c
            mayor = b
    elif b < a and  b < c:
        menor = b
        if  a < c :
            medio = a
            mayor = c
        else:
            medio = c
            mayor = a
    else:
        menor = c
        if  a < b :
            medio = a
            mayor = b
        else :
            medio = b
            mayor = a
    print(f'El numero menor es:{menor} , El numero mayor es: {mayor}')