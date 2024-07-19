import graficos
import pandas as pd

def graficoJSON():
    # Codigo de graficacion utilizando las funciones creadas por nosotros
    call = graficos.paises("./data.csv")
    nombre_pais = input("Escribe el nombre de un pais: ")
    pais_encontrado = graficos.buscar_pais(call, nombre_pais)
    printable = graficos.jsonFormat(pais_encontrado)
    print(printable)
    years, population = graficos.poblacion(pais_encontrado)
    graficos.graficaBarras(years, population, nombre_pais)
    return None

def graficoPandas():
    #Codigo de graficacion utilizando pandas
    df = pd.read_csv("data.csv")
    nombre_usuario = input("Escribe el nombre para el grafico: ")
    countries = df["Country"].values == nombre_usuario
    percentages = df["World Population Percentage"].values
    graficos.graficaBarras(countries, percentages, nombre_usuario)
    return None

def opciones():
    menu = int(input("Ingresa algunas de las siguientes opciones:\n1.Mostrar graficoJSON\n2.Mostrar garfico Pandas\n"))
    if menu == 1:
        graficoJSON()
    elif menu == 2:
        graficoPandas()
    else:
        False

def run():
    opciones()

if __name__ == '__main__':
    run()
