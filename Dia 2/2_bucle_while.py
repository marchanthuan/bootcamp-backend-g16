# while puede convertirse en un bucle infinito

numero = 10
# while se ejecutara hasta que la conidcion sea verdadera
# while primero valida la condicion y luego ejecuta el codigo
while numero < 20:
    print('hola')
    print(numero)
    numero += 1

# en python no existe el do-while
valor = input('Por favor ingresa un numero: ')
print(valor)

# adivina el numero
print('***** ESTE ES UN BINGO *******')
numero = 75
numero_adivinado = 0
while numero_adivinado != numero:
    # todos los valores que le pasemos al input se capturara como string
    numero_adivinado = int(input('Adivina el numero: '))

