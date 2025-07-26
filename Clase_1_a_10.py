# --------------------------------------------------------
# Clase 1
# --------------------------------------------------------
# print('Me encanta la pizza')
# print('Es muy bueno')


# --------------------------------------------------------
# clase 2 Variebles y tipos de datos
# --------------------------------------------------------

# String
# nombre = 'Sebastian' #String
# print('Hola ' + nombre)
# print(type(nombre)) #Muestra el tipo de dato

# apellido = 'Jeldes' #String
# nombre_completo = 'Hola ' + nombre + apellido
# print(nombre_completo)

# entero
# edad = 21 #int
# edad2 = '21'
# #edad = edad + 1
# edad += 1
# edad2 += 1 da error
# una es un int y lña otra es un string
# print(type(edad))
# print(type(edad2))

# entero con cadena de texto
# print('Tu edad es ' + str(edad))

# Float
# altura = 1.75 #float
# print(altura)
# print(type(altura))

# print('Tu altura es: ' + str(altura))

# Boolean
# humano = False

# print(humano)
# print(type(humano))
# print('Eres un humano: ' + str(humano))


#--------------------------------------------------------
# Clase 3 Asignaciones multiples
#--------------------------------------------------------

# nombre = 'Sebastian'
# edad = 21
# atractivo = True

# nombre, edad, atractivo = 'Sebastian', 21, True

# print(nombre)
# print(edad)
# print(atractivo)

# nombre1 = 10
# nombre2 = 10
# nombre3 = 10
# nombre4 = 10

# nombre1 = nombre2 = nombre3 = nombre4 = 10
# print(nombre1)
# print(nombre2)
# print(nombre3)
# print(nombre4)

# --------------------------------------------------------
# Clase 4 Metodos de cadenas de texto
# --------------------------------------------------------

# nombre = 'Sebastian'
# apellido = 'jeldes'
# edad = 21

# contar caracteres de cadenas de texto
# print(len(nombre))
# print(len(apellido))

#Encontrar la posicion de un caracter
# print(nombre.find("s"))

# primera palabra en mayusculas
# print(apellido.capitalize())

# Convertir a mayusculas
# print(nombre.upper())  

# # Convertir a minusculas
# print(nombre.lower())

# Verifica si es un numero
# print(edad.isdigit())  

# Verifica si es un caracter alfabetico
# print(nombre.isalpha())

# # Cuenta cuantas veces aparece un caracter en una cadena de texto
# print(nombre.count('a'))  

# Reemplaza un caracter por otro
# print(nombre.replace('a', 'o'))  

# Repite una cadena de texto
# print(nombre * 4)

# --------------------------------------------------------
# Clase 5 Convertir tipos de datos
# --------------------------------------------------------

# x = 1
# y = 2.5
# z = '3'

# x = str(x)
# y = int(y)
# z = float(z)

# print(x)  
# print(y)  
# print(z)  

# print(str(x))
# print(int(y))
# print(float(z))


# --------------------------------------------------------
# Clase 6 Ingresar texto en python
# --------------------------------------------------------

# String (Entrada por defecto)
# nombre = input('Cual es tu nombre? ')

# int
# edad = int(input('Cual es tu edad? '))

# float
# altura = float(input('Cual es tu altura? '))

# print('Hola ' + nombre)
# print('Tu edad es: ' + str(edad))
# print('Tu altura es: ' + str(altura))

# --------------------------------------------------------
# Clase 7 Funciones matematicas
# --------------------------------------------------------

# Importar biblioteca math
# import math

# PI = 3.14
# PI2 = -3.14


# x = 2
# y = 1
# z = 3

# # Redondear un numero
# print(round(PI))

# # Redondea hacia arriba
# print(math.ceil(PI))  

# # redondea hacia abajo
# print(math.floor(PI))

# # Valor absoluto
# print(abs(PI2))

# # Potencia
# print(pow(PI, 2))  

# # Raiz cuadrada
# print(math.sqrt(420))

# # Maximo
# print(max(x, y, z))  

# # Minimo
# print(min(x, y, z))

# --------------------------------------------------------
# Clase 8 Como manipular cadenas de texto
# --------------------------------------------------------


# nombre = 'Sebastian Jeldres'

# #indice de iniciacion
# primer_nombre = nombre[0]

# #indice de finalizacion
# primer_nombre1 = nombre[0:9] # o usar nombre[:9]

# # Extraer apellido
# apellido = nombre[10:17] # o usar nombre[10:]

# # Extraer caracteres con saltos
# nombre2 = nombre[0:9:2] # o usar nombre[::2]

# print(primer_nombre)
# print(primer_nombre1)
# print(apellido)
# print(nombre2)

# Invierte la cadena de texto
# nombre_invertido = nombre[::-1]
# print(nombre_invertido) 


#Funcioon slide

# website = 'https://wwwyoutube.com'

# slice = slice(11, -4)  # Empieza desde el indice 11 y termina 4 caracteres antes del final
# print(website[slice])  # Imprime 'youtube' 


# --------------------------------------------------------
# Clase 9 Instrucciones if, else y elif
# --------------------------------------------------------

# edad = int(input('Cual es tu edad? '))

# if edad >= 18:
#     print('Eres mayor de edad')
# elif edad < 18:
#     print('Eres menor de edad')


