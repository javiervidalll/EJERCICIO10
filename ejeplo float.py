import stats_data as sd

lista = []
while True:
    numeros = input("introduce los nnumeros: ")
    if numeros == "fin":
        break
    numeros = float(numeros)
    lista.append(numeros)
calculo_stats = sd.StatsData(lista)

print("lista de numeros: ", calculo_stats)
print("media : ",calculo_stats.mean)
print("mediana:  ", calculo_stats.median)
print("varianza: ", calculo_stats.varance)