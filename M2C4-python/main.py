### Ejercicio 1
from decimal import Decimal

mi_lista = ["manzanas", "bananas", "peras"]
mi_tupla = (1,2,3)
mi_float = 3.14
mi_entero = 11
mi_decimal = Decimal("0.1")
mi_diccionario = {
    "tarea": "comprar",
    "producto" : "frutas",
    "realizado" : False
}


### Ejercicio 2
import math

mi_float = 3.14
resultado = math.ceil(mi_float)

print(resultado)  


### Ejercicio 3
import math

mi_float = 3.14
raiz = math.sqrt(mi_float)
print(raiz)  #1.772004514666935

raiz = mi_float**0.5
print(raiz)  #1.772004514666935


### Ejercicio 4

#Si sabemos el nombre de la clave:
primer_elemento = mi_diccionario['tarea']
print(primer_elemento)

#Si no lo sabemos:
elemento_uno = next(iter(mi_diccionario.items()))
print(elemento_uno)

primera_clave = next(iter(mi_diccionario))
print(primera_clave)

primer_valor = next(iter(mi_diccionario.values()))
print(primer_valor)


### Ejercicio 5
mi_tupla = (1,2,3)
print(mi_tupla[1])


### Ejercicio 6
mi_lista = ["manzanas", "bananas", "peras"]
mi_lista.append("naranjas")
print(mi_lista)


### Ejercicio 7
mi_lista[0] = "uvas"
print(mi_lista)


### Ejercicio 8
mi_lista.sort()
print(mi_lista)


### Ejercicio 9
mi_tupla = mi_tupla + (4,)
print(mi_tupla)