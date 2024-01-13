# guardar varios valores en una misma variable. Puedo agrupar varios valores en una variable

# Listas
# Coleccion de datos que se pueden modifiar, es ordenada (porque maneja indices)
alumnos = ['Victor', 'Hiroito', 'Marco', 'Angel', 'Bryan', 'Samael', 'Claudia']

# Todas las listas comienzan con la posicion cero
print(alumnos[0])
print(alumnos[4]) # cuenta la posicion

# Para saber el contenido (longitud) de datos. cuenta y no utililza las posiciones
print(len(alumnos)) # len cuenta todo los elementos

print(alumnos[-3]) # cuenta de la derecha a izquierda

# si queremos recorrer la lista de derecha a izquierda usaremos numeros negativos
print(alumnos[-1]) # ultimo de la lista
print(alumnos[len(alumnos)-1])

# aregar elementos a una lista ya crada
alumnos.append('Franklin')

print('Lista con valor añadido=>', alumnos)

# remover un elemento de la lista lo podemos guardar en una variable
alumno_eliminado = alumnos.pop(2)
print(alumnos)
print('Valor eliminado=>', alumno_eliminado)

# del o delete podemos eliminar variables eliminar posiciones de la lista y otras cosas
del alumnos[0]
print('Lista sin valor eliminado=> ', alumnos)

#cada vez qye se elimina una pposicon de la lista, todas las demas posiciones ocupan ese lugar disponible

# modificar el valor de una posicion de una lista
alumnos[0] = 'Eduardo'
print('Lista con valor modificado=>', alumnos)

#limpiamos toda la lista y la dejamos vacia
# remover toda la lista y la dejamos vacia
alumnos.clear()
print(alumnos)

# las listas pueden contener varios tipos de datos
mixto = ['Lunes', 10, False, 80.5, [1, 2, 3]]

print(mixto)

ejercicio = [1, 2, 3, [4, 5, 6]]

# Devolver el valor de 3
print(ejercicio[2])
# Como puedo devolver el valor de 5
print(ejercicio[3][1])

# Tuplas
# Es una lista que no se puede modificar y es ordenada (indices)
# Se usa para guardar valores que jamas van a poder cambiar
meses = ('Enero', 'Febrero', 'Marzo', 'Abril')

print(meses[0])

# No se puede realizar funciones de agregar, eliminar, modificar a una Tupla
# meses.append('Mayo')
# meses.pop(2)

data = ('Juan', 'Roberto', [1, 2, 3, ['Eduardo', 'Frank', [4, 5, 6, ['Tepsup', 'Codigo', ]]]])
print(data[2][3][0])
print(data[2][3][2][3][1])

# Set (Conjuntos)
# Es desordenada (sin indices) y modificable
colores = {'Negro', 'Blanco', 'Guinda', 'Violeta'}

print(colores)
colores.add('Azul')
print(colores)

print('Verde' in colores) # false - no esta en la lista
print('Blanco' in colores) # True - si esta en la lista
colores.remove('Blanco')
print('Blanco' in colores) # false - ya no esta en la lista

# Diccionarios
# Ordenados, PERO por llaves y modificables
persona = {
    'nombre': 'Eduardo',
    'edad': 31,
    'nacionalidad': 'peruano',
    'apellido': 'de rivero'
}
print(persona.keys()) # devuelve los nombre de las llaves
print(persona.values()) # devuelve los valores
print(persona['edad'])
# print(persona['edades']) # en JAVASCRIPT si no existe me retorna undefined, aca lanza error

# modificar una llave
persona['nombre'] = 'Juancito'
persona['calzado'] = 'Zapatos' # si la llave no existe, entonces la creara
print(persona)

persona = {
    'nombre':"Roberto",
    'edad': 40,
    'hobbies': ['Nada', 'Pescar', 'Jugar videojuegos'],
    'idiomas': [
        {
            'nombre': 'Ingles',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'Frances',
            'nivel': 'Basico'
        }
    ],
    'habilidades': {'Puntual', 'Economico', 'Proactivo'},
    'debilidades': ('Mentiroso', 'Resentido', 'Comelon')
}

# 1. Darme la Edad
print(persona['edad'])

# 2. Mostrar los hobbies
print(persona['hobbies'])

# 3. Mostrar el ultimo hobbie ingresado
print(persona['hobbies'][-1])

# 4. Mostrar los idiomas SOLO SUS NOMBRE
print(persona['idiomas'][0]['nombre'])
print(persona['idiomas'][1]['nombre'])

# 5. Ver si es Proactivo
print('Proactivo' in persona['habilidades'])

# 6. Ver cuantas debilidades tiene (cantidad)
print(len(persona['debilidades']))
