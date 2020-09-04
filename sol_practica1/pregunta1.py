def hola(nombre):
    tamaño_nombre = len(nombre) 
    if tamaño_nombre >= 1:
        print(f'Hola, {nombre}')
    else:
        print('Hola mundo')
nombre = input('Ingresa tu nombre:')
hola(nombre)