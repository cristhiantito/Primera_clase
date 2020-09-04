def divisible(n,x,y):
    if n%x == 0 and n%y == 0 :
        print(True)
    else:
        print(False)

n = float(input('Ingresa el numero: '))
print('Ingresa los parametros de divisibilidad')
x = float(input('Ingresa x: '))
y = float(input('Ingresa y: '))
divisible(n,x,y)
