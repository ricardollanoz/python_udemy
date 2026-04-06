#Sistema generador unico ID
import random

nombre = input("Ingrese su nombre: ").lower() #solo los dos primeros digitos
apellido = input("Ingrese su apellido: ").lower()#solo los dos primeros digitos
ano_nacimiento = (input("Ingrese su año de nacimiento: ")) #solo los dos ultimos digitos
num_aleatorio = random.randint(0,9999)

print(f"su codigo es: {nombre[:2]}{apellido[:2]}{ano_nacimiento[2:]}{num_aleatorio:04d}")

