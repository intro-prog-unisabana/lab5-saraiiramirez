import utils

mensaje = input("Please type your message\n")

invertido = utils.flip(mensaje)
cantidad = utils.count_letters(mensaje, 'a')

result = invertido + str(cantidad)

print("Your encoded message is :", result)