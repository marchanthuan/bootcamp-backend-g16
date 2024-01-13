print('hola')
print('fin')

edad = 13
nacionalidad = 'VENEZOLANO'
# if => si
if edad > 18 and nacionalidad == 'PERUANO':
    print('Puedes votar')

#else > sino
else:
    print('llamare a tus padres')


# if => si
if edad > 18 or nacionalidad == 'PERUANO':
    print('Puedes votar')

#else > sino
else:
    print('llamare a tus padres')


if edad > 18:
    print('puedes votar')
# elif sino si
elif edad > 15:
    print('te falta poco para votar')
else:
    print('que haces aqui')

# segun el sexo y la estarura hacer lo siguiente
# si es masculino
    # si mide mas de 1.50 entonces indicar que no hay prendas
    # si mide entre 1.30 y 1.49 indicar que si hay ropa
    # y su mide menos de 1.30 indicar que no hay prendas
# si es femenino
    # si mida mas de 1.40 indicar que no hay prendas
    # si mide entre 1.10 y 1.49 indicar que si hay
    # si mide menos de 1.10 indicar que no hay

sexo = 'Masculino'
estatura = 1.35
# output > SI HAY ROPA

sexo = 'Masculino'
estatura = 1.80
# output > NO HAY ROPA

sexo = 'Femenino'
estatura = 1.20
# output > SI HAY ROPA

sexo = 'Femenino'
estatura = 1.08
# output > NO HAY ROPA

sexo = 'Femenino'
estatura = 1.08

if sexo == 'Masculino':
    if estatura > 1.50:
        print('Hombre, No hay ropa...')
    else:
        if estatura>1.30:
            print('Hombre, Si hay ropa...')
        else:
            print('Hombre, No hay ropa...')
else:
    if estatura > 1.40:
        print('Mujer, No hay ropa...')
    else:
        if estatura>1.10:
            print('Mujer, Si hay ropa...')
        else:
            print('Mujer, No hay ropa...')



if sexo == 'Masculino':
    if estatura > 1.30 and estatura <1.40:
        print('Hombre, Si hay ropa...')
    else:
        print('Hombre, No hay ropa...')
else:
    if estatura > 1.49 and estatura <1.10:
        print('Mujer, Si hay ropa...')
    else:
        print('Mujer, No hay ropa...')



if sexo == 'Masculino':
    if estatura > 1.30 and estatura <1.49:
        print('Hombre, Si hay ropa...')
    else:
        print('Hombre, No hay ropa...')
elif sexo == 'femenino':
    if estatura > 1.10 and estatura <1.40:
        print('Mujer, Si hay ropa...')
    else:
        print('Mujer, No hay ropa...')
        # o usamos el pass o colocamos la logica
        # pass > pasa (no hace nada pro nos permite dejar la condicional vacia)
        pass

# operador TERNARIO
# condicion que sirve para ejeuctarse en una sola linea y en base a la condicion RETORNARA un valor o otr
    
# si el usuario es PERUANO pagara 5 soles si es EXTRANJERO pagara 8 soles
nacionalidad = 'ECUATORIANO'

if nacionalidad == 'PERUANO':
    print('pague 5 soles')
else:
    print('pague 8 soles')

# OPERADOR TERNARIO
# no se puede utilizar en sus resultados PALABRAS NO CLAVE
# TERNARIO  resultado TRUE  IF     CONDICION                   resultado FALSE
resultado = 'pague 5 soles' if nacionalidad == 'PERUANO' else 'pague 8 soles'

print(resultado)

