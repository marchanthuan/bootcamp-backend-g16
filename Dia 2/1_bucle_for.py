alumnos = ['Angel', 'Bryan', 'Carlos', 'Hiroito', 'Claudia', 'Samael', 'Marco']

for alumno in alumnos:
    print(alumno)

# for se puede utilizar con string (textos)
frase = 'No hay mal que por bien no venga'
letra = 'j' # no es necesario definir la variable para ser usada en el for
for letra in frase:
    print(letra)

print(letra) # termina con la ultima letra de la frase, reemplazando la letra original

#imprimir el texto pero sin espacios
#pista: usar el if y el pass
for letra in frase:
    if letra == ' ':
        pass
    else:
        print(letra)
#pista: usar el if sin el else
if letra != ' ':
    print(letra)

#forma 3
#continue > termina el ciclo actual (la iteraccion en camino) y no permit e hacer nada mas luego
# del continue
# continue solo se puede utilizar dentro de un llop (FOR, WHILE)

for letra in frase:
    if letra == ' ':
        continue
    print(letra)

# Forma 4
    # operador ternario SOLO SE PUEDE colocar en sus resultados PALABRAS NO CLAVE
    # None > nada / nadie
    # para definir una variable y esta no queremos colocar un valor inicial podermos usar la palabra None
    # Si no queremos realizar nada en un operador ternario podemos colocarlo ahi
print('*********')
for letra in frase:
    None if letra == ' ' else print(letra)

#la variable edad tiene un contenido vacaio, esto en javascrip seira como undefinid
edad = None

print('-----------------------------------')
# range > si quiero realizar un for manual sin uso de listas, tuplas set o textos
#range (limite) > el for se ejecutara hasta que el valor sea menor que el tope (limite)

for numero in range(4):
    print(numero)


for numero in range(1,4): # range(inicio, limite)
    print(numero)

for numero in range(1, 10, 2): #range(inicio, limite, incremento/decremeto)
    print(numero)

#
texto = 'Hola me llamo eduardo'
vocales = ['a', 'e', 'i', 'o', 'u']

print('j' in vocales)
print('e' in vocales)

# Iterar la variable tezto y ver cuantas covlaes hay
#Respuesta: Hay 9 vocales
contador = 0
for letra in texto:
     if letra in vocales: 
         contador = contador + 1

print('Hay ' + str(contador) + ' vocales')

print('Hay', contador, 'vocales')

# {} donde coloquemos llaves {} ahi vamos a colocar una variable que puede ser numero, texto, bool, etc.
print('Hay {} vocales'.format(contador))

# al colocar la f antes de las comillas estaremos indicando que lo que vaya dentro de las llaves sera codigo pythion
# dentro de ellas podermos utilizar variables y operaciones
print(f'Hay {contador} vocales')

# %s que convierta el valor que le vamos a pasar a un foamto texto
print('Hay %s vocales' % (contador))

# % porcentaje se conoce como modulo
print(99/5) #cociente
print(99 % 5) # residuo entero = 4
print(99 // 5 ) # cociente entero, sin la parte decimal = 19

# Utilizando range realice
range(1,56)
#quiero saber cuantos numeros pares tengo
# Resulado: Hay 27 numeros pares
numero % 2 == 0 # es un numero par

contador = 0
print(contador)
for numero in range(1,56):
    if numero % 2 == 0: 
         contador += 1
print('Hay', contador, 'numeros pares')


