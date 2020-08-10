print('Ingrese monto en soles:')
soles = input()
valor_por_dolar = float (0.28)
total = round (float(soles) * float(valor_por_dolar),2) 
print (f'Su monto es ${total}')

