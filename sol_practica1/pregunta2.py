def area(longitut,ancho):
    if longitut == ancho:
        area_cuadrado = longitut**2
        print(f'su figura es un cuadrado area: {area_cuadrado}')
    else:
        area_rectangulo = longitut * ancho
        print(f'su fiigura es un rectangulo area: {area_rectangulo}')

     

longitut = float(input('ingresa tu longitu: '))
ancho = float(input('ingrese el ancho: '))
area(longitut,ancho)

