import graficos

def run():
    call = graficos.paises("./data.csv")
    nombre_pais = input("Escribe el nombre de un pais: ")
    pais_encontrado = graficos.buscar_pais(call, nombre_pais)
    printable = graficos.jsonFormat(pais_encontrado)
    print(printable)
    years, population = graficos.poblacion(pais_encontrado)
    graficos.graficaBarras(years, population, nombre_pais)

if __name__ == '__main__':
    run()
