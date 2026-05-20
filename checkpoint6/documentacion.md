## 🐍 Documentación Python para CheckPoint 6

- **Autor:** Ailén
- **Nivel:** Iniciación
- **Formato:** Markdown
- **Fecha:** Mayo 2026

---

## 📄Tabla de contenidos:

1. [¿Para qué usamos Clases en Python?](#1-clases-en-python)

2. [¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?](#2-metodos-en-python)

3. [¿Cuáles son los tres verbos de API?](#3-verbos-de-apis-en-python)

4. [¿Es MongoDB una base de datos SQL o NoSQL?](#4-mongodb)

5. [¿Qué es una API?](#5-que-es-una-api)

6. [¿Qué es Postman?](#6-postman)

7. [¿Qué es el polimorfismo?](#7-que-es-el-polimorfismo)

8. [¿Qué es un método dunder?](#8-metodo-dunder)

9. [¿Qué es un decorador de python?](#9-decoradores-en-python)



## 1. Clases en Python

Una clase es una plantilla o molde que define cómo se creará un objeto. Permiten empaquetar datos (atributos) y comportamientos (métodos) juntos, lo que facilita la creación de objetos.

### ¿Para qué las usamos?
Las usamos principalmente para organizar el código y aplicar un concepto llamado Programación Orientada a Objetos (POO). Sus mayores ventajas son:

- Evitan duplicar código: Defines el comportamiento una sola vez en la clase y lo reutilizas mil veces.

- Organización: Juntan los datos (variables) y las acciones (funciones) en un solo lugar lógico.

- Modelar el mundo real: Hacen que el código sea más fácil de entender porque programamos pensando en "cosas" (usuarios, productos, enemigos, facturas) en lugar de solo líneas de texto sueltas.

### Conceptos Claves

- **Constructor (__init__):** 
Es un método especial que se ejecuta automáticamente cuando creas un objeto a partir de la clase. Se utiliza para asignar los valores iniciales a los atributos.
- **self:** 
Representa la instancia actual de la clase. Es obligatorio incluirlo como el primer parámetro en los métodos para poder acceder a los atributos propios del objeto.
- **Instancias:**
 Son los objetos individuales creados a partir de la clase. Cada instancia tiene sus propios datos

**Ejemplo sin clases (desordenado):**
```python
marca_coche1 = "toyota"
modelo_coche1 = "hilux"
 
marca_coche2 = "volkswagen"
modelo_coche2 = "amarok"
```
 
**Ejemplo con clases (organizado):**
```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
coche1 = Coche("toyota", "hilux")
coche2 = Coche("volkswagen", "amarok")
 
print(coche1.marca)  # toyota
print(coche2.modelo)    # amarok
```
 
Con una clase, podemos crear todos los coches que queramos usando el mismo molde.