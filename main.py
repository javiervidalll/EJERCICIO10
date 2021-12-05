
"""marca coche, modelo, combustible y cilindrada"""
"""ejemplo bucle"""
data = list ()
while True:
    entrada = float(input("Siguiente dato (-999 para terminar)?: "))
    if entrada != -999.0:
        data.append(entrada)
    else:
        break
for dato in data:
    print ("Dato: ", dato)

listacoche = []
while True:
    marcacoche = float(input("Escribe una marca de coches: "))
    if marcacoche != "fin":

    modelocoche = input("Escribe un modelo de coche de la marca escogida: ")
    combustible = input("¿Qué combustible utiliza?: ")
    cilindrada = input("¿Cuál es su cilindrada?: ")
    linea = {}
    linea["Marcacoche"] = marcacoche
    linea["Modelo"] = modelocoche
    linea["Combustible"] = combustible
    linea["Cilindrada"] = cilindrada
        listacoche.append(linea)
else:


