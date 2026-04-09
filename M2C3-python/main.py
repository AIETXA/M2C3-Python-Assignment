### Ejercicio 1

texto = 'Lista de la compra'
numero = 12
lista = ['banana', 'manzana', 'kiwi', 'mandarina']
boolean = False


### Ejercicio 2

texto_two = texto[0:3]
print(texto_two)


### Ejercicio 3

primer_elemento = lista[0]
print(primer_elemento)


### Ejercicio 4

suma = numero + 10
print(suma)


### Ejercicio 5

print(lista[-1])


### Ejercicio 6

names = 'harry,alex,susie,jared,gail,conner'

nueva_lista = names.split(',')
print(nueva_lista)


### Ejercicio 7

espacio = texto.index(' ')
primera_palabra = texto[:espacio]
a_mayuscula = primera_palabra.upper()
combinacion = a_mayuscula + texto[espacio:]
print(combinacion)


### Ejercicio 8

print(f'El número que elegí es el {numero}')

### Ejercicio 9

print('hello world')


#Ejercicio practico , reemplazar palabra.

cadena = 'Hola, ¿que tal?'

posicion = cadena.index('Hola')

nueva_cadena = cadena.replace('Hola', 'adiós')
print(nueva_cadena)

