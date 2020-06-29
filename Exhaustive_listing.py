#Algoritmo de numeracion exhaustiva.
#tambien llamado "adivina y verifica".
#Las computadoras actuales son muy rápidas, este es uno de los primeros algoritmos que debo tratar.

objetivo = int(input('Escoge un entero, por favor (con raíz cuadrada exacta):'))
respuesta = 0

while respuesta**2 < objetivo:
    #print(respuesta)             #Esto es un print statement.
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f' Lo siento, el numero {objetivo} no tiene raiz cuadrada exacta.')