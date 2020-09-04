def over_the_road(numero_casa,longitud_calle):
    casas_izquierda=[]
    casas_derecha=[]
    c=1
    while True:
        if c % 2 == 0:
            casas_derecha.append(c)
        else:
            casas_izquierda.append(c)
        if len(casas_izquierda)==longitud_calle and len(casas_derecha)==longitud_calle:
            break
        c += 1
    print(casas_izquierda)
    print(casas_derecha)
    over_the_road(1,3)
    