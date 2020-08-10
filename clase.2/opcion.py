def imprimir_mensaje (opcion):
    print( f"""
     Hola
    ¿como estas?
    eligiste la {opcion}
    Adios
    """)
opcion = input('ingresa tu opcion')
if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4':
    imprimir_mensaje (opcion)
else :
    print ('Escogio mal')