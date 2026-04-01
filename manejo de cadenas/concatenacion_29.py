# saludo = "hola" 
# nombre= "ricardo"
# print(saludo + " " +nombre)

# nombre = "ricardo"
# edad = 25
# print(f"Hola {nombre}, tienes {edad}")

"""Funcion len"""

# saludo = "hola mundo"
# contador = len(saludo)
# print(f"el saludo tiene {contador} caracteres")

"""Metodo upper y lower"""

# # saludo = "holA mUndo"
# conv_mayuscula = saludo.upper()
# print(conv_mayuscula)
# conv_minuscula = saludo.lower()
# print(conv_minuscula)

"""con este metodo podemos convertir a mayuscula y minuscula"""


"""35. SUbcadenas"""
# nombre = "Ricardo".upper()

# subcadena = nombre[0:3] 
# print(subcadena)
# subcadena2 = nombre[:3] 
# print(subcadena2)
# subcadena3 = nombre[3:]
# print(subcadena3)
# subcadena4 = nombre[-3:]
# print(subcadena4)
# subcadena5 = nombre[::-1]
# print(subcadena5)

"""FUncion replace"""
# saludo = "Hola mundo, mundo".upper()
# nuevo = saludo.replace("MUNDO", "rick")
# print(nuevo)

# "funcion finde, te ayuda  a saber el indice por el que comienza la palabra"
# saludo = "hola mundo"
# indice = saludo.find("mundo")
# print(indice)


"RETO. GENERADOR DE EMAIL"
"Crea un programa para generar email a partir de los siguientes datos nombre, empresa, domicilio"
nombre = input("Escriba su nombre:").lower().replace(" ",".")
empresa = input("Escriba nombre de la empresa: ").lower().replace(" ", "")
domicilio = input("Escriba domiciminio").lower()
print(f"Email: {nombre}@{empresa}.{domicilio}")