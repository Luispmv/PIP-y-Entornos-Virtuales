import csv
import matplotlib.pyplot as plt
import json

# La funcion paises convierte un csv en diccionario y los valores en string que son decimales los convierte a flotantes
def paises(path):
    informacion_paises = []
    string_info_values = ["CCA3","Country","Capital","Continent"]
    with open(path, "r") as csvfile:
        datos_paises = csv.reader(csvfile, delimiter=",")
        llaves = next(datos_paises)
        for valor in datos_paises:
            diccionario_paises = dict(zip(llaves, valor))
            informacion_paises.append(diccionario_paises)

        for pais in informacion_paises:
            for key, value in pais.items():
                if key not in string_info_values:
                    pais[key] = float(value)
    return informacion_paises

#Busca un pais por su nombre
def buscar_pais(informacion_paises, nombre_pais):
    for pais in informacion_paises:
        if pais["Country"] == nombre_pais:
            return pais
    return None

# La funcion jsonFormat utiliza el modulo json para imprimir en un formato JSON un diccionario indicado por su index
def jsonFormat(call):
    return json.dumps(call,indent=4)

# La funcion poblacion toma un diccionario como argumento y arma un nuevo diccionario para despues sacar sus claves y valores como arrays separados
def poblacion(paises):
    poblacion = {
        "2022": paises["2022 Population"],
        "2020": paises["2020 Population"],
        "2015": paises["2015 Population"],
        "2010": paises["2010 Population"],
        "2000": paises["2000 Population"],
        "1990": paises["1990 Population"],
        "1980": paises["1980 Population"],
        "1970": paises["1970 Population"]
    }
    años = [item for item in poblacion.keys()]
    poblacion = [item for item in poblacion.values()]
    return años, poblacion

# La funcion graficaPastel nos devuelve una grafica de pastel con los datos devueltos por la funcion poblacion
def graficaBarras(labels, values, name):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.title(f"Poblacion de {name} a traves de los años")
    fig.canvas.manager.set_window_title(f"Evolucion de la poblacion de {name} a lo largo de los años")
    plt.show()



