# La variable puede ser declarada de diferente manera, sin establecer el tipo por defecto
nombre = 'Eduardo'
nombre = 12
nombre = False
nombre = '2013-12-12'

# Creo la variable para indicar el estado civil de la persona
soltero = False

# El comentario es muy importante para mantener nuestro codigo documentado
print(nombre)

numero1 = 10

numero2 = 40

print(type(numero1))
resultado = numero1 + numero2
print(resultado)

# Si queremos realizar una sumatoria entre un texto y un numero no es posible
#Si la sumatoria se realiza entre dos string (texto) esta sera una concatenacion

numero1 = '80'
numero2 = "40"

resultado = numero1 + numero2
print(resultado)

#para convertir de un tipo de dato a otro, utilizo el tipo de dato que quiero convertir
# tengo que esta seguro que el calor fuente pueda ser convertido
print(type(numero1))

convertir_entero = int(numero1)

print(type(convertir_entero))

#Tipos de variables tenemos en Python

# INT (enteros)
numero = 10
numero = -10

# FLOAT (flotantes que tiene decimal)
# Si ponemos coma esto se puede confundir con un tipo de dato especial (ARREGLO, TUPLA, DICCIONARIO)
calificacion = 10.4

# BOOLEAN Booleano True o False
vacunado = False

# STRING (text) puedes usar comilla simple y comilla doble, indiferente
nombre = 'Eduardo "El Carnicero"'
nombre = "Eduard'o"

# TENEMOS LA TRIPLE COMILLA SIMPLE O DOBLE si queremos tener un texto que contenga saltos de linea usamos la triple comilla o triple doble comilla
texto = '''
Era ua manaña de enero.
Los pajaron cantaban...
'''
texto2 = """
Y en eso, una señora
Muy amablemente me sonrio y me dijo "...."
"""
print(texto)
print(texto2)

# definir varias variables con , coma
curso, grupo, mes, dia, hora, inicio = 'Backend', 'G16', 'Enero', 11, 20, 45

print(curso, grupo, mes, dia, hora, inicio )

# forman de declarar  variables, funciones, clases, metodos
snake_case = 'snake_Case'
nombre_completo = 'Eduardo de Rivero Manrique'

cameCase = 'camelCase'

PascalCase = 'PascalCase'



