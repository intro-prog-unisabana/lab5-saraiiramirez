from utils import flip, count_letters

mensaje = input("Please type your message\n")

invertido = flip(mensaje)
cantidad = count_letters(mensaje, 'a')

mensaje_codificado = invertido + str(cantidad)

print("Your encoded message is :", mensaje_codificado)