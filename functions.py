def promedio_estudiante (calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    
    suma_total = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = float(suma_total / cantidad)

    return promedio

notas = [85, 92, 78]
print(promedio_estudiante(notas))