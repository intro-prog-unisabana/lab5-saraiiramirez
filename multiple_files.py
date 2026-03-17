from utils import *

mensaje = input("Please type your message\n")

invertido = flip(mensaje)
cantidad = count_letters(mensaje)

mensaje_codificado = invertido + str(cantidad)

print(f"Your encoded message is : {mensaje_codificado}")