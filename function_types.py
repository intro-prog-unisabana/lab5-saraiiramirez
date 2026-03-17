def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] = lista[i] + valor

def calc_avg(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

def print_normalized(lista):
    print(lista)

datos = [2.0, 4.0, 6.0, 8.0]

prom = calc_avg(datos)         # 5.0
list_shift(datos, -prom)       # datos se convierte en [-3.0, -1.0, 1.0, 3.0]
print_normalized(datos)        # imprime [-3.0, -1.0, 1.0, 3.0]