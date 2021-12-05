#tipo de datos estadisticos de una lista,imprimir los atributos con mean,median y variance
import statistics as st
class StatsData:
    def   __init__(self, lista):
        self.l_data = lista
        self.mean = st.mean(self.l_data)
        self.median = st.median(self.l_data)
        self.varance = st.variance(lista)